import os
SECRET_KEY = 'mi_clave_ultra_segura_1234'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/portafolio_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
