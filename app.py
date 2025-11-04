from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Ejemplo de modelo
class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puesto = db.Column(db.String(100))
    empresa = db.Column(db.String(100))
    fecha_inicio = db.Column(db.String(50))
    fecha_fin = db.Column(db.String(50))
    descripcion = db.Column(db.Text)

@app.route('/')
def index():
    experiencias = Experiencia.query.all()
    return render_template('index.html', experiencias=experiencias)

if __name__ == '__main__':
    app.run(debug=True)
