from extensions import db

class Habilidad(db.Model):
    __tablename__ = 'habilidades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    porcentaje = db.Column(db.Integer)
    tipo = db.Column(db.String(50))
    icono = db.Column(db.String(255))


    def __repr__(self):
        return f"<Habilidad {self.nombre} ({self.tipo})>"
