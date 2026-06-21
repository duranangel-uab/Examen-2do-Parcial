from app.extensions import db

class Pedido(db.Model):
    __tablename__ = 'pedido'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    total = db.Column(db.Float, nullable=False, default=0)
    estado = db.Column(db.String(20), nullable=False, default='pendiente')
    
    # Claves foráneas
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesa.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    
    def __repr__(self):
        return f"Pedido #{self.id}"