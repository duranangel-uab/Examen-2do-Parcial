from flask import jsonify, request, current_app
from flask_appbuilder import BaseView, expose, has_access
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.plato import Plato
from app.models.categoria import Categoria
from app.models.mesa import Mesa
from app.models.cliente import Cliente
from app.models.empleado import Empleado
from app.models.pedido import Pedido
from app.models.detalle_pedido import DetallePedido
import os
import uuid


EXTENSIONES_PERMITIDAS = {"png", "jpg", "jpeg", "gif", "webp"}


# Estado del carrito "en vivo", compartido en memoria entre el POS y la
# pantalla del cliente (segundo monitor). No se guarda en base de datos
# porque es información temporal/transitoria mientras se construye una
# venta; basta con una variable de proceso para este alcance académico.
_CARRITO_EN_VIVO = {"items": [], "total": 0, "ultimo_pedido": None}


class PosView(BaseView):
    """
    Punto de Venta (POS): permite registrar una venta nueva eligiendo
    platos de un catálogo visual, un cliente, una mesa y un empleado.
    Disponible para los 3 roles del sistema (Admin, Supervisor, Usuario).
    """

    route_base = "/pos"
    default_view = "index"

    @expose("/")
    @has_access
    def index(self):
        categorias = Categoria.query.order_by(Categoria.nombre).all()
        platos = (
            Plato.query.filter_by(disponible=True)
            .order_by(Plato.nombre)
            .all()
        )
        mesas = Mesa.query.order_by(Mesa.numero).all()
        clientes = Cliente.query.order_by(Cliente.nombre).all()
        empleados = Empleado.query.filter_by(activo=True).order_by(Empleado.nombre).all()

        return self.render_template(
            "pos.html",
            categorias=categorias,
            platos=platos,
            mesas=mesas,
            clientes=clientes,
            empleados=empleados,
        )

    @expose("/cliente-nuevo", methods=["POST"])
    @has_access
    def cliente_nuevo(self):
        """Crea un cliente rápido desde el POS (nombre y apellido como
        mínimo) y lo devuelve para agregarlo de inmediato al select."""
        data = request.get_json(silent=True) or {}
        nombre = (data.get("nombre") or "").strip()
        apellido = (data.get("apellido") or "").strip()

        if not nombre or not apellido:
            return jsonify({"ok": False, "error": "Nombre y apellido son obligatorios."})

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=(data.get("email") or "").strip() or None,
            telefono=(data.get("telefono") or "").strip() or None,
        )
        db.session.add(cliente)
        db.session.commit()

        return jsonify({
            "ok": True,
            "cliente": {"id": cliente.id, "nombre": f"{cliente.nombre} {cliente.apellido}"},
        })

    @expose("/registrar-venta", methods=["POST"])
    @has_access
    def registrar_venta(self):
        """Crea un Pedido nuevo junto con sus líneas de DetallePedido,
        a partir del carrito enviado desde el POS. Si el pedido es "para
        llevar", no requiere mesa; si no, marca la mesa elegida como
        'ocupada'."""
        data = request.get_json(silent=True) or {}

        cliente_id = data.get("cliente_id")
        mesa_id = data.get("mesa_id")
        empleado_id = data.get("empleado_id")
        para_llevar = bool(data.get("para_llevar"))
        carrito = data.get("carrito") or []

        if not cliente_id or not empleado_id:
            return jsonify({"ok": False, "error": "Cliente y empleado son obligatorios."})

        if not para_llevar and not mesa_id:
            return jsonify({"ok": False, "error": "Selecciona una mesa, o marca 'Para llevar'."})

        if not carrito:
            return jsonify({"ok": False, "error": "El carrito está vacío."})

        # Validamos que el cliente y el empleado existan
        cliente = Cliente.query.get(cliente_id)
        empleado = Empleado.query.get(empleado_id)
        if not cliente or not empleado:
            return jsonify({"ok": False, "error": "Cliente o empleado no válido."})

        mesa = None
        if not para_llevar:
            mesa = Mesa.query.get(mesa_id)
            if not mesa:
                return jsonify({"ok": False, "error": "Mesa no válida."})

        pedido = Pedido(
            cliente_id=cliente.id,
            mesa_id=mesa.id if mesa else None,
            empleado_id=empleado.id,
            estado="pendiente",
            para_llevar=para_llevar,
            total=0,
        )
        db.session.add(pedido)
        db.session.flush()  # para obtener pedido.id antes del commit

        total = 0.0
        for item in carrito:
            plato = Plato.query.get(item.get("plato_id"))
            cantidad = int(item.get("cantidad") or 0)
            if not plato or cantidad <= 0:
                continue

            subtotal = plato.precio * cantidad
            detalle = DetallePedido(
                pedido_id=pedido.id,
                plato_id=plato.id,
                cantidad=cantidad,
                subtotal=subtotal,
            )
            db.session.add(detalle)
            total += subtotal

        pedido.total = total
        if mesa:
            mesa.estado = "ocupada"

        db.session.commit()

        # Guardamos el último carrito confirmado para que la pantalla del
        # cliente (/pos/pantalla-cliente) pueda mostrar el resumen final.
        _CARRITO_EN_VIVO["items"] = []
        _CARRITO_EN_VIVO["total"] = 0
        _CARRITO_EN_VIVO["ultimo_pedido"] = {"id": pedido.id, "total": total}

        return jsonify({"ok": True, "pedido_id": pedido.id, "total": total})

    @expose("/cambiar-imagen-plato", methods=["POST"])
    @has_access
    def cambiar_imagen_plato(self):
        """Cambia la imagen de un plato directamente desde el POS, ya
        sea subiendo un archivo desde el equipo o pegando una URL."""
        plato_id = request.form.get("plato_id")
        plato = Plato.query.get(plato_id) if plato_id else None
        if not plato:
            return jsonify({"ok": False, "error": "Plato no válido."})

        archivo = request.files.get("archivo")
        url = (request.form.get("url") or "").strip()

        if archivo and archivo.filename:
            extension = archivo.filename.rsplit(".", 1)[-1].lower() if "." in archivo.filename else ""
            if extension not in EXTENSIONES_PERMITIDAS:
                return jsonify({
                    "ok": False,
                    "error": "Formato de imagen no permitido (usa png, jpg, jpeg, gif o webp).",
                })

            nombre_archivo = secure_filename(f"plato_{plato.id}_{uuid.uuid4().hex[:8]}.{extension}")
            carpeta_uploads = os.path.join(
                current_app.root_path, "static", "uploads", "platos"
            )
            os.makedirs(carpeta_uploads, exist_ok=True)
            ruta_completa = os.path.join(carpeta_uploads, nombre_archivo)
            archivo.save(ruta_completa)

            plato.imagen_url = f"/static/uploads/platos/{nombre_archivo}"

        elif url:
            plato.imagen_url = url
        else:
            return jsonify({"ok": False, "error": "Sube un archivo o pega una URL de imagen."})

        db.session.commit()
        return jsonify({"ok": True, "imagen_url": plato.imagen_url})

    @expose("/cerrar-venta", methods=["POST"])
    @has_access
    def cerrar_venta(self):
        """Marca un pedido como 'entregado' (pago realizado al final del
        consumo) y libera automáticamente su mesa, si tenía una."""
        data = request.get_json(silent=True) or {}
        pedido_id = data.get("pedido_id")

        pedido = Pedido.query.get(pedido_id) if pedido_id else None
        if not pedido:
            return jsonify({"ok": False, "error": "Pedido no encontrado."})

        pedido.estado = "entregado"
        if pedido.mesa_id:
            mesa = Mesa.query.get(pedido.mesa_id)
            if mesa:
                mesa.estado = "disponible"

        db.session.commit()
        return jsonify({"ok": True})

    @expose("/actualizar-carrito-vivo", methods=["POST"])
    @has_access
    def actualizar_carrito_vivo(self):
        """Recibe el estado actual del carrito (mientras se construye la
        venta) para que la pantalla del cliente lo muestre en vivo."""
        data = request.get_json(silent=True) or {}
        _CARRITO_EN_VIVO["items"] = data.get("items") or []
        _CARRITO_EN_VIVO["total"] = data.get("total") or 0
        return jsonify({"ok": True})

    @expose("/carrito-vivo", methods=["GET"])
    @has_access
    def carrito_vivo(self):
        """Devuelve el estado actual del carrito en vivo, consultado
        periódicamente por la pantalla del cliente (polling)."""
        return jsonify({"ok": True, "carrito": _CARRITO_EN_VIVO})

    @expose("/pantalla-cliente")
    @has_access
    def pantalla_cliente(self):
        """Pantalla pensada para un segundo monitor orientado al
        cliente: muestra en vivo lo que el cajero/mesero va agregando
        al carrito, incluyendo la imagen de cada plato. Cuando no hay
        ningún pedido en construcción, muestra un slideshow con fotos
        de los platos disponibles, a modo de vitrina."""
        imagenes_slideshow = [
            p.imagen_url
            for p in Plato.query.filter(
                Plato.disponible.is_(True), Plato.imagen_url.isnot(None)
            ).all()
            if p.imagen_url
        ]
        return self.render_template(
            "pos_pantalla_cliente.html", imagenes_slideshow=imagenes_slideshow
        )
