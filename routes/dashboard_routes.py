from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from models.datos_personales import DatosPersonales
from models.educacion import Educacion
from models.proyectos import Proyecto
from models.habilidades import Habilidad
from models.experiencia import Experiencia
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

@dashboard_bp.route('/guardar-experiencia', methods=['POST'])
def guardar_experiencia():
    experiencia_id = request.form.get('id')
    if experiencia_id:
        experiencia = Experiencia.query.get(experiencia_id)
    else:
        experiencia = Experiencia()

    experiencia.puesto = request.form.get('puesto')
    experiencia.empresa = request.form.get('empresa')
    experiencia.fecha_inicio = request.form.get('fecha_inicio')
    experiencia.fecha_fin = request.form.get('fecha_fin')
    experiencia.descripcion = request.form.get('descripcion')
    experiencia.es_actual = 'es_actual' in request.form

    db.session.add(experiencia)
    db.session.commit()
    flash('Experiencia guardada correctamente.', 'success')
    return redirect(url_for('main.index'))

@dashboard_bp.route('/guardar-educacion', methods=['POST'])
def guardar_educacion():
    educacion_id = request.form.get('id')
    if educacion_id:
        educacion = Educacion.query.get(educacion_id)
    else:
        educacion = Educacion()

    educacion.instituto = request.form.get('instituto')
    educacion.titulo = request.form.get('titulo')
    educacion.fecha_inicio = request.form.get('fecha_inicio')
    educacion.fecha_fin = request.form.get('fecha_fin')
    educacion.descripcion = request.form.get('descripcion')

    db.session.add(educacion)
    db.session.commit()
    flash('Educación guardada correctamente.', 'success')
    return redirect(url_for('main.index'))
@dashboard_bp.route('/guardar-proyecto', methods=['POST'])
def guardar_proyecto():
    proyecto_id = request.form.get('id')
    if proyecto_id:
        proyecto = Proyecto.query.get(proyecto_id)
    else:
        proyecto = Proyecto()

    proyecto.nombre = request.form.get('nombre')
    proyecto.descripcion = request.form.get('descripcion')
    proyecto.fecha = request.form.get('fecha')
    proyecto.enlace = request.form.get('enlace')

    if 'imagen' in request.files:
        file = request.files['imagen']
        if file.filename != '':
            filename = f"proyecto_{proyecto.id or 'nuevo'}.jpg"
            file.save(os.path.join('static/images', filename))
            proyecto.imagen = f"images/{filename}"

    db.session.add(proyecto)
    db.session.commit()
    flash('Proyecto guardado correctamente.', 'success')
    return redirect(url_for('main.index'))
@dashboard_bp.route('/guardar-habilidad', methods=['POST'])
def guardar_habilidad():
    habilidad_id = request.form.get('id')
    if habilidad_id:
        habilidad = Habilidad.query.get(habilidad_id)
    else:
        habilidad = Habilidad()

    habilidad.nombre = request.form.get('nombre')
    habilidad.porcentaje = request.form.get('porcentaje')
    habilidad.tipo = request.form.get('tipo')

    db.session.add(habilidad)
    db.session.commit()
    flash('Habilidad guardada correctamente.', 'success')
    return redirect(url_for('main.index'))
