from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.user import Usuario
from forms.login_form import LoginForm
from forms.register_form import RegisterForm  # 👈 importamos el formulario de registro

auth_bp = Blueprint('auth', __name__)

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html', form=form)

# REGISTER
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Verificar si el usuario ya existe
        existing_user = Usuario.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso.', 'warning')
            return redirect(url_for('auth.register'))

        # Crear usuario nuevo
        hashed_password = generate_password_hash(form.password.data)
        new_user = Usuario(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Usuario registrado correctamente. ¡Ahora podés iniciar sesión!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

# LOGOUT
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('main.index'))
