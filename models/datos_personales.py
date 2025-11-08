from extensions import db

class DatosPersonales(db.Model):
    __tablename__ = 'datos_personales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100))
    foto_perfil = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    redes_sociales = db.Column(db.JSON)
    banner_imagen = db.Column(db.String(255))
