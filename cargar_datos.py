from app import create_app, db
from app.models.cliente import Cliente
from app.models.mesa import Mesa
from app.models.empleado import Empleado
from app.models.categoria import Categoria
from app.models.ingrediente import Ingrediente
from app.models.plato import Plato
from app.models.plato_ingrediente import PlatoIngrediente
from app.models.pedido import Pedido
from app.models.detalle_pedido import DetallePedido
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    print("🔄 Cargando datos de ejemplo...")
    
    # 1. Crear categorías
    categorias = [
        {"nombre": "Entradas", "descripcion": "Platos para empezar"},
        {"nombre": "Platos principales", "descripcion": "Platos fuertes"},
        {"nombre": "Postres", "descripcion": "Dulces tentaciones"},
        {"nombre": "Bebidas", "descripcion": "Refrescos y jugos"},
        {"nombre": "Ensaladas", "descripcion": "Opciones saludables"},
    ]
    
    for cat in categorias:
        if not Categoria.query.filter_by(nombre=cat["nombre"]).first():
            categoria = Categoria(nombre=cat["nombre"], descripcion=cat["descripcion"])
            db.session.add(categoria)
            print(f"✅ Categoría creada: {cat['nombre']}")
    
    db.session.commit()
    
    # 2. Crear ingredientes
    ingredientes = [
        {"nombre": "Harina", "unidad": "gramos", "stock": 5000, "precio_unitario": 2.5, "stock_minimo": 500},
        {"nombre": "Huevo", "unidad": "unidades", "stock": 100, "precio_unitario": 1.0, "stock_minimo": 20},
        {"nombre": "Leche", "unidad": "mililitros", "stock": 10000, "precio_unitario": 1.2, "stock_minimo": 1000},
        {"nombre": "Aceite", "unidad": "mililitros", "stock": 5000, "precio_unitario": 3.0, "stock_minimo": 500},
        {"nombre": "Sal", "unidad": "gramos", "stock": 1000, "precio_unitario": 0.5, "stock_minimo": 100},
        {"nombre": "Azúcar", "unidad": "gramos", "stock": 2000, "precio_unitario": 1.0, "stock_minimo": 200},
        {"nombre": "Carne", "unidad": "gramos", "stock": 3000, "precio_unitario": 15.0, "stock_minimo": 500},
        {"nombre": "Pollo", "unidad": "gramos", "stock": 4000, "precio_unitario": 12.0, "stock_minimo": 500},
        {"nombre": "Arroz", "unidad": "gramos", "stock": 5000, "precio_unitario": 2.0, "stock_minimo": 500},
        {"nombre": "Tomate", "unidad": "unidades", "stock": 50, "precio_unitario": 1.5, "stock_minimo": 10},
        {"nombre": "Cebolla", "unidad": "unidades", "stock": 30, "precio_unitario": 1.0, "stock_minimo": 10},
        {"nombre": "Queso", "unidad": "gramos", "stock": 2000, "precio_unitario": 8.0, "stock_minimo": 200},
        {"nombre": "Mantequilla", "unidad": "gramos", "stock": 1000, "precio_unitario": 5.0, "stock_minimo": 100},
        {"nombre": "Ajo", "unidad": "dientes", "stock": 100, "precio_unitario": 0.5, "stock_minimo": 20},
        {"nombre": "Papas", "unidad": "gramos", "stock": 5000, "precio_unitario": 2.0, "stock_minimo": 500},
        {"nombre": "Pasta", "unidad": "gramos", "stock": 3000, "precio_unitario": 3.0, "stock_minimo": 300},
    ]
    
    for ing in ingredientes:
        if not Ingrediente.query.filter_by(nombre=ing["nombre"]).first():
            ingrediente = Ingrediente(
                nombre=ing["nombre"],
                unidad=ing["unidad"],
                stock=ing["stock"],
                precio_unitario=ing["precio_unitario"],
                stock_minimo=ing["stock_minimo"]
            )
            db.session.add(ingrediente)
            print(f"✅ Ingrediente creado: {ing['nombre']}")
    
    db.session.commit()
    
    # 3. Crear platos
    platos = [
        {
            "nombre": "Milanesa con papas",
            "descripcion": "Milanesa de carne con papas fritas",
            "precio": 45.0,
            "categoria": "Platos principales",
            "ingredientes": [
                {"nombre": "Carne", "cantidad": 200},
                {"nombre": "Papas", "cantidad": 300},
                {"nombre": "Huevo", "cantidad": 2},
                {"nombre": "Aceite", "cantidad": 50},
                {"nombre": "Sal", "cantidad": 5},
            ]
        },
        {
            "nombre": "Pollo al horno",
            "descripcion": "Pollo horneado con papas y especias",
            "precio": 50.0,
            "categoria": "Platos principales",
            "ingredientes": [
                {"nombre": "Pollo", "cantidad": 300},
                {"nombre": "Papas", "cantidad": 200},
                {"nombre": "Ajo", "cantidad": 3},
                {"nombre": "Aceite", "cantidad": 30},
                {"nombre": "Sal", "cantidad": 5},
            ]
        },
        {
            "nombre": "Ensalada César",
            "descripcion": "Ensalada con pollo, queso y aderezo César",
            "precio": 35.0,
            "categoria": "Ensaladas",
            "ingredientes": [
                {"nombre": "Pollo", "cantidad": 150},
                {"nombre": "Queso", "cantidad": 50},
                {"nombre": "Huevo", "cantidad": 1},
                {"nombre": "Sal", "cantidad": 3},
                {"nombre": "Aceite", "cantidad": 20},
            ]
        },
        {
            "nombre": "Arroz con pollo",
            "descripcion": "Arroz con pollo y verduras",
            "precio": 40.0,
            "categoria": "Platos principales",
            "ingredientes": [
                {"nombre": "Arroz", "cantidad": 200},
                {"nombre": "Pollo", "cantidad": 200},
                {"nombre": "Cebolla", "cantidad": 1},
                {"nombre": "Ajo", "cantidad": 2},
                {"nombre": "Sal", "cantidad": 5},
            ]
        },
        {
            "nombre": "Torta de chocolate",
            "descripcion": "Torta de chocolate con crema",
            "precio": 25.0,
            "categoria": "Postres",
            "ingredientes": [
                {"nombre": "Harina", "cantidad": 200},
                {"nombre": "Huevo", "cantidad": 3},
                {"nombre": "Azúcar", "cantidad": 150},
                {"nombre": "Mantequilla", "cantidad": 100},
                {"nombre": "Leche", "cantidad": 100},
            ]
        }
    ]
    
    for plato_data in platos:
        categoria = Categoria.query.filter_by(nombre=plato_data["categoria"]).first()
        if not categoria:
            print(f"❌ Categoría no encontrada: {plato_data['categoria']}")
            continue
        
        plato = Plato(
            nombre=plato_data["nombre"],
            descripcion=plato_data["descripcion"],
            precio=plato_data["precio"],
            categoria_id=categoria.id,
            disponible=True
        )
        db.session.add(plato)
        db.session.flush()
        
        for ing_data in plato_data["ingredientes"]:
            ingrediente = Ingrediente.query.filter_by(nombre=ing_data["nombre"]).first()
            if ingrediente:
                plato_ingrediente = PlatoIngrediente(
                    plato_id=plato.id,
                    ingrediente_id=ingrediente.id,
                    cantidad=ing_data["cantidad"]
                )
                db.session.add(plato_ingrediente)
        
        print(f"✅ Plato creado: {plato_data['nombre']}")
    
    db.session.commit()
    
    # 4. Crear mesas
    for i in range(1, 11):
        if not Mesa.query.filter_by(numero=i).first():
            mesa = Mesa(numero=i, capacidad=4, estado="disponible")
            db.session.add(mesa)
    print("✅ 10 mesas creadas")
    
    db.session.commit()
    
    # 5. Crear empleados
    empleados = [
        {"nombre": "Juan", "apellido": "Pérez", "cargo": "Administrador", "email": "juan@eldeseo.com"},
        {"nombre": "María", "apellido": "López", "cargo": "Cajero", "email": "maria@eldeseo.com"},
        {"nombre": "Carlos", "apellido": "García", "cargo": "Cocinero", "email": "carlos@eldeseo.com"},
    ]
    
    for emp in empleados:
        if not Empleado.query.filter_by(email=emp["email"]).first():
            empleado = Empleado(
                nombre=emp["nombre"],
                apellido=emp["apellido"],
                cargo=emp["cargo"],
                email=emp["email"],
                activo=True
            )
            db.session.add(empleado)
            print(f"✅ Empleado creado: {emp['nombre']} {emp['apellido']}")
    
    db.session.commit()
    
    # 6. Crear pedidos de ejemplo
    clientes = [
        {"nombre": "Ana", "apellido": "Gómez", "email": "ana@email.com"},
        {"nombre": "Luis", "apellido": "Martínez", "email": "luis@email.com"},
        {"nombre": "Sofía", "apellido": "Ramírez", "email": "sofia@email.com"},
    ]
    
    for cli in clientes:
        if not Cliente.query.filter_by(email=cli["email"]).first():
            cliente = Cliente(
                nombre=cli["nombre"],
                apellido=cli["apellido"],
                email=cli["email"]
            )
            db.session.add(cliente)
    db.session.commit()
    
    # Crear pedidos
    platos_list = Plato.query.all()
    clientes_list = Cliente.query.all()
    mesas_list = Mesa.query.all()
    empleados_list = Empleado.query.all()
    
    if platos_list and clientes_list and mesas_list and empleados_list:
        for i in range(5):
            pedido = Pedido(
                cliente_id=clientes_list[i % len(clientes_list)].id,
                mesa_id=mesas_list[i % len(mesas_list)].id,
                empleado_id=empleados_list[i % len(empleados_list)].id,
                estado="entregado",
                fecha=datetime.now() - timedelta(days=i*2)
            )
            db.session.add(pedido)
            db.session.flush()
            
            # Agregar detalles al pedido
            for j in range(2):
                plato = platos_list[(i + j) % len(platos_list)]
                detalle = DetallePedido(
                    pedido_id=pedido.id,
                    plato_id=plato.id,
                    cantidad=j + 1,
                    subtotal=plato.precio * (j + 1)
                )
                db.session.add(detalle)
                pedido.total += detalle.subtotal
            
            print(f"✅ Pedido #{pedido.id} creado")
    
    db.session.commit()
    
    print("🎉 ¡Todos los datos de ejemplo cargados exitosamente!")
    print(f"📊 Resumen:")
    print(f"   - Categorías: {Categoria.query.count()}")
    print(f"   - Ingredientes: {Ingrediente.query.count()}")
    print(f"   - Platos: {Plato.query.count()}")
    print(f"   - Mesas: {Mesa.query.count()}")
    print(f"   - Empleados: {Empleado.query.count()}")
    print(f"   - Clientes: {Cliente.query.count()}")
    print(f"   - Pedidos: {Pedido.query.count()}")