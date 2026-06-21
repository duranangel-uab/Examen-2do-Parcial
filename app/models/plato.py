from app import db

class Plato(db.Model):
    __tablename__ = 'plato'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(300), nullable=True)
    precio = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    tiempo_preparacion = db.Column(db.Integer, nullable=True)
    
    # Clave foránea a Categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    
    # Relación con Categoria
    categoria = db.relationship('Categoria', backref='platos')
    
    def __repr__(self):
        return f"{self.nombre} (${self.precio:.2f})"