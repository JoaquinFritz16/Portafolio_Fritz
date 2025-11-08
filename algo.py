from werkzeug.security import generate_password_hash
hashed_password = generate_password_hash("contraseña_segura")
print(hashed_password)  # Copia este hash
