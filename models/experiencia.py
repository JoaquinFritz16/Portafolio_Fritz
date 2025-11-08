from extensions import db

class Experiencia(db.Model):
    __tablename__ = 'experiencia'

    id = db.Column(db.Integer, primary_key=True)
    puesto = db.Column(db.String(100), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    descripcion = db.Column(db.Text)
    es_actual = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Experiencia {self.puesto} en {self.empresa}>"
