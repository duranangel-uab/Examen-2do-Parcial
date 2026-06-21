from app.extensions import db

class PlatoIngrediente(db.Model):
    __tablename__ = 'plato_ingrediente'
    
    # Clave primaria compuesta
    plato_id = db.Column(db.Integer, db.ForeignKey('plato.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
    cantidad = db.Column(db.Float, nullable=False)
    
    # Relaciones
    plato = db.relationship('Plato', backref='ingredientes')
    ingrediente = db.relationship('Ingrediente', backref='platos')
    
    def __repr__(self):
        return f"{self.cantidad} {self.ingrediente.unidad} de {self.ingrediente.nombre}"