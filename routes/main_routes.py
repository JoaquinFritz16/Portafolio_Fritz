from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models.datos_personales import DatosPersonales
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    datos_personales = DatosPersonales.query.first()
    return render_template(
        'index.html',
        datos_personales=datos_personales,
        is_admin=current_user.is_authenticated and current_user.username == 'admin'
    )
