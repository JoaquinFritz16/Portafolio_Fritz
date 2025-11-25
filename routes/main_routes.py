from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models.datos_personales import DatosPersonales
from models.educacion import Educacion
from models.experiencia import Experiencia
from models.proyectos import Proyecto
from models.habilidades import Habilidad
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    datos_personales = DatosPersonales.query.first()
    experiencias = Experiencia.query.all()
    educaciones = Educacion.query.all()
    proyectos = Proyecto.query.all()
    habilidades = Habilidad.query.all()
    return render_template(
        'index.html',
        datos_personales=datos_personales,
        experiencias=experiencias,
        educaciones=educaciones,
        proyectos=proyectos,
        habilidades=habilidades,
        is_admin=current_user.is_authenticated and current_user.username == 'admin'
    )
