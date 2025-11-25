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
from datetime import datetime



dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')  # Ruta principal del dashboard
@login_required
def index():
    if not current_user.es_admin:
        flash('No tienes permisos para acceder al dashboard.', 'danger')
        return redirect(url_for('main.index'))
    # Obtener los datos personales para mostrar en el formulario
    datos = DatosPersonales.query.first()
    experiencias = Experiencia.query.all()  # Asegúrate de que esta línea esté presente
    educaciones = Educacion.query.all()
    proyectos = Proyecto.query.all()
    habilidades = Habilidad.query.all()
    return render_template('dashboard/index.html', datos=datos, experiencias=experiencias, educaciones=educaciones, proyectos=proyectos, habilidades=habilidades)

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
@login_required
def guardar_experiencia():
    if not current_user.es_admin:
        flash('No tienes permisos para guardar experiencias.', 'danger')
        return redirect(url_for('dashboard.index'))

    experiencia_id = request.form.get('id')
    if experiencia_id:
        experiencia = Experiencia.query.get(experiencia_id)
    else:
        experiencia = Experiencia()

    experiencia.puesto = request.form.get('puesto')
    experiencia.empresa = request.form.get('empresa')
    experiencia.fecha_inicio = datetime.strptime(request.form.get('fecha_inicio'), '%Y-%m-%d').date()
    fecha_fin = request.form.get('fecha_fin')
    experiencia.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date() if fecha_fin else None
    experiencia.descripcion = request.form.get('descripcion')
    experiencia.es_actual = 'es_actual' in request.form

    db.session.add(experiencia)
    db.session.commit()
    flash('Experiencia guardada correctamente.', 'success')
    return redirect(url_for('dashboard.index'))



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
@login_required
def guardar_habilidad():
    if not current_user.es_admin:
        flash('No tienes permisos para guardar habilidades.', 'danger')
        return redirect(url_for('dashboard.index'))

    habilidad_id = request.form.get('id')
    if habilidad_id:
        habilidad = Habilidad.query.get(habilidad_id)
    else:
        habilidad = Habilidad()

    habilidad.nombre = request.form.get('nombre')
    habilidad.porcentaje = int(request.form.get('porcentaje'))
    habilidad.tipo = request.form.get('tipo')
    habilidad.icono = request.form.get('icono')

    db.session.add(habilidad)
    db.session.commit()
    flash('Habilidad guardada correctamente.', 'success')
    return redirect(url_for('dashboard.index'))

@dashboard_bp.route('/eliminar-habilidad/<int:habilidad_id>', methods=['POST'])
@login_required
def eliminar_habilidad(habilidad_id):
    if not current_user.es_admin:
        flash('No tienes permisos para eliminar habilidades.', 'danger')
        return redirect(url_for('dashboard.index'))

    habilidad = Habilidad.query.get(habilidad_id)
    if habilidad:
        db.session.delete(habilidad)
        db.session.commit()
        flash('Habilidad eliminada correctamente.', 'success')
    else:
        flash('Habilidad no encontrada.', 'danger')

    return redirect(url_for('dashboard.index'))

@dashboard_bp.route('/eliminar-experiencia/<int:experiencia_id>', methods=['POST'])
@login_required
def eliminar_experiencia(experiencia_id):

    if not current_user.es_admin:
        flash('No tienes permisos para eliminar experiencias.', 'danger')
        return redirect(url_for('dashboard.index'))

    experiencia = Experiencia.query.get(experiencia_id)
    if experiencia:
        db.session.delete(experiencia)
        db.session.commit()
        flash('Experiencia eliminada correctamente.', 'success')
    else:
        flash('No se encontró la experiencia.', 'danger')

    return redirect(url_for('dashboard.index'))


@dashboard_bp.route('/eliminar-educacion/<int:educacion_id>', methods=['POST'])
@login_required
def eliminar_educacion(educacion_id):
    if not current_user.es_admin:
        flash('No tienes permisos para eliminar educación.', 'danger')
        return redirect(url_for('dashboard.index'))

    educacion = Educacion.query.get(educacion_id)
    if educacion:
        db.session.delete(educacion)
        db.session.commit()
        flash('Educación eliminada correctamente.', 'success')
    else:
        flash('Educación no encontrada.', 'danger')

    return redirect(url_for('dashboard.index'))

@dashboard_bp.route('/eliminar-proyecto/<int:proyecto_id>', methods=['POST'])
@login_required
def eliminar_proyecto(proyecto_id):
    if not current_user.es_admin:
        flash('No tienes permisos para eliminar proyectos.', 'danger')
        return redirect(url_for('dashboard.index'))

    proyecto = Proyecto.query.get(proyecto_id)
    if proyecto:
        db.session.delete(proyecto)
        db.session.commit()
        flash('Proyecto eliminado correctamente.', 'success')
    else:
        flash('Proyecto no encontrado.', 'danger')

    return redirect(url_for('dashboard.index'))


@dashboard_bp.route('/obtener-experiencia/<int:experiencia_id>', methods=['GET'])
@login_required
def obtener_experiencia(experiencia_id):
    if not current_user.es_admin:
        return jsonify({'error': 'No tienes permisos'}), 403

    experiencia = Experiencia.query.get(experiencia_id)
    if experiencia:
        return jsonify({
            'id': experiencia.id,
            'puesto': experiencia.puesto,
            'empresa': experiencia.empresa,
            'fecha_inicio': experiencia.fecha_inicio.strftime('%Y-%m-%d') if experiencia.fecha_inicio else '',
            'fecha_fin': experiencia.fecha_fin.strftime('%Y-%m-%d') if experiencia.fecha_fin else '',
            'descripcion': experiencia.descripcion,
            'es_actual': experiencia.es_actual
        })
    else:
        return jsonify({'error': 'Experiencia no encontrada'}), 404


@dashboard_bp.route('/obtener-habilidad/<int:habilidad_id>', methods=['GET'])
@login_required
def obtener_habilidad(habilidad_id):
    if not current_user.es_admin:
        return jsonify({'error': 'No tienes permisos'}), 403

    habilidad = Habilidad.query.get(habilidad_id)
    if habilidad:
        return jsonify({
            'id': habilidad.id,
            'nombre': habilidad.nombre,
            'porcentaje': habilidad.porcentaje,
            'tipo': habilidad.tipo,
            'icono': habilidad.icono
        })
    else:
        return jsonify({'error': 'Habilidad no encontrada'}), 404

@dashboard_bp.route('/obtener-proyecto/<int:proyecto_id>', methods=['GET'])
@login_required
def obtener_proyecto(proyecto_id):
    if not current_user.es_admin:
        return jsonify({'error': 'No tienes permisos'}), 403

    proyecto = Proyecto.query.get(proyecto_id)
    if proyecto:
        return jsonify({
            'id': proyecto.id,
            'nombre': proyecto.nombre,
            'descripcion': proyecto.descripcion,
            'fecha': proyecto.fecha.strftime('%Y-%m-%d') if proyecto.fecha else '',
            'enlace': proyecto.enlace,
            'imagen': proyecto.imagen
        })
    else:
        return jsonify({'error': 'Proyecto no encontrado'}), 404


@dashboard_bp.route('/obtener-educacion/<int:educacion_id>', methods=['GET'])
@login_required
def obtener_educacion(educacion_id):
    if not current_user.es_admin:
        return jsonify({'error': 'No tienes permisos'}), 403

    educacion = Educacion.query.get(educacion_id)
    if educacion:
        return jsonify({
            'id': educacion.id,
            'instituto': educacion.instituto,
            'titulo': educacion.titulo,
            'fecha_inicio': educacion.fecha_inicio.strftime('%Y-%m-%d') if educacion.fecha_inicio else '',
            'fecha_fin': educacion.fecha_fin.strftime('%Y-%m-%d') if educacion.fecha_fin else '',
            'descripcion': educacion.descripcion
        })
    else:
        return jsonify({'error': 'Educación no encontrada'}), 404
