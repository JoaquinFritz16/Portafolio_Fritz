from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, current_app
from flask_login import current_user
from models.datos_personales import DatosPersonales
from models.educacion import Educacion
from models.experiencia import Experiencia
from models.proyectos import Proyecto
from models.habilidades import Habilidad
import pdfkit
import imgkit
import os

main_bp = Blueprint('main', __name__)

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
WKHTMLTOIMAGE_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"

pdf_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
img_config = imgkit.config(wkhtmltoimage=WKHTMLTOIMAGE_PATH)

PDF_OPTIONS = {
    'enable-local-file-access': None,
    'quiet': '',
    'load-error-handling': 'ignore',
    'load-media-error-handling': 'ignore'
}

IMG_OPTIONS = {
    'enable-local-file-access': None,
    'quiet': '',
    'load-error-handling': 'ignore',
    'load-media-error-handling': 'ignore'
}
@main_bp.route('/')
def index():
    return render_template(
        'index.html',
        datos_personales=DatosPersonales.query.first(),
        experiencias=Experiencia.query.all(),
        educaciones=Educacion.query.all(),
        proyectos=Proyecto.query.all(),
        habilidades=Habilidad.query.all(),
        is_admin=current_user.is_authenticated and current_user.username == 'admin'
    )


@main_bp.route('/descargar-imagen')
def descargar_imagen():
    html_render = _render_portfolio_to_html()

    temp_html = os.path.join(current_app.root_path, "static", "temp_export.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_render)

    output_img = os.path.join(current_app.root_path, "static", "portfolio_image.jpg")

    imgkit.from_file(
        temp_html,
        output_img,
        config=img_config,
        options=IMG_OPTIONS
    )

    return send_file(output_img, as_attachment=True)


@main_bp.route('/descargar-pdf')
def descargar_pdf():
    html_render = _render_portfolio_to_html()

    temp_html = os.path.join(current_app.root_path, "static", "temp_export.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_render)

    output_pdf = os.path.join(current_app.root_path, "static", "portfolio.pdf")

    pdfkit.from_file(
        temp_html,
        output_pdf,
        configuration=pdf_config,
        options=PDF_OPTIONS
    )

    return send_file(output_pdf, as_attachment=True)


def _render_portfolio_to_html():


    html = render_template(
        'index.html',
        datos_personales=DatosPersonales.query.first(),
        experiencias=Experiencia.query.all(),
        educaciones=Educacion.query.all(),
        proyectos=Proyecto.query.all(),
        habilidades=Habilidad.query.all(),
        is_admin=False,
        export_mode=True
    )

    static_path = os.path.join(current_app.root_path, "static").replace("\\", "/")
    html = html.replace('/static/', f'file:///{static_path}/')


    html = html.replace(
        'https://cdn.jsdelivr.net/npm/sortablejs@1.14.0/Sortable.min.css',
        ''
    )
    html = html.replace(
        'https://cdn.jsdelivr.net/npm/sortablejs@1.14.0/Sortable.min.js',
        ''
    )

    return html
