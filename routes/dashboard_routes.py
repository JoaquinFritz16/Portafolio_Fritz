from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from models.datos_personales import DatosPersonales
from extensions import db
import os

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')  # Ruta principal del dashboard
@login_required
def index():
    if not current_user.es_admin:
        flash('No tienes permisos para acceder al dashboard.', 'danger')
        return redirect(url_for('main.index'))
    # Obtener los datos personales para mostrar en el formulario
    datos = DatosPersonales.query.first()
    return render_template('dashboard/index.html', datos=datos)

@dashboard_bp.route('/guardar-orden', methods=['POST'])
@login_required
def guardar_orden():
    if not current_user.es_admin:
        return jsonify({'error': 'No tienes permisos'}), 403
    nuevo_orden = request.json.get('orden')
    # Aquí guardas el nuevo orden en la base de datos o en una sesión
    return jsonify({'success': True})

@dashboard_bp.route('/editar-banner', methods=['POST'])
@login_required
def editar_banner():
    if not current_user.es_admin:
        flash('No tienes permisos para editar el banner.', 'danger')
        return redirect(url_for('main.index'))
    # Obtener los datos personales
    datos = DatosPersonales.query.first()
    if not datos:
        datos = DatosPersonales()
    # Actualizar los campos
    datos.nombre = request.form.get('nombre')
    datos.titulo = request.form.get('titulo')
    # Manejar la subida de la imagen del banner
    if 'banner_imagen' in request.files:
        file = request.files['banner_imagen']
        if file.filename != '':
            filename = 'banner-bg.jpg'  # Nombre fijo para simplificar
            file.save(os.path.join(current_app.root_path, 'static/images', filename))
            datos.banner_imagen = f'images/{filename}'
    db.session.commit()
    flash('Banner actualizado correctamente.', 'success')
    return redirect(url_for('main.index'))