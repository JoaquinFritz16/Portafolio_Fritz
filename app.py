from flask import Flask
from config import Config
from extensions import db, login_manager


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from routes.main_routes import main_bp
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@login_manager.user_loader
def load_user(user_id):
    from models.user import Usuario  
    return Usuario.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Terminado