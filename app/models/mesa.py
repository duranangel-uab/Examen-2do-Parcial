from app.extensions import db

class Mesa(db.Model):
    __tablename__ = 'mesa'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False, unique=True)
    capacidad = db.Column(db.Integer, nullable=False, default=4)
    estado = db.Column(db.String(20), nullable=False, default='disponible')
    ubicacion = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f"Mesa {self.numero} ({self.estado})"