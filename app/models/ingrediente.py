from app import db

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    unidad = db.Column(db.String(30), nullable=False)
    stock = db.Column(db.Float, nullable=False, default=0)
    precio_unitario = db.Column(db.Float, nullable=False, default=0)
    stock_minimo = db.Column(db.Float, nullable=False, default=0)
    
    def __repr__(self):
        return f"{self.nombre} ({self.stock} {self.unidad})"