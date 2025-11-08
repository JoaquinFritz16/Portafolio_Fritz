from extensions import db

class Educacion(db.Model):
    __tablename__ = 'educacion'

    id = db.Column(db.Integer, primary_key=True)
    instituto = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    descripcion = db.Column(db.Text)

    def __repr__(self):
        return f"<Educacion {self.titulo} en {self.instituto}>"

