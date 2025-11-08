from extensions import db

class Proyecto(db.Model):
    __tablename__ = 'proyectos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    fecha = db.Column(db.Date)
    enlace = db.Column(db.String(255))
    imagen = db.Column(db.String(255))

    def __repr__(self):
        return f"<Proyecto {self.nombre}>"
