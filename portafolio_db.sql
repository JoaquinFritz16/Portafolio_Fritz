-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS portafolio_db;
USE portafolio_db;

-- Tabla de usuarios (para el login y autenticación)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL  -- Guardar contraseñas hasheadas
);

-- Tabla de datos personales
CREATE TABLE IF NOT EXISTS datos_personales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    titulo VARCHAR(100),
    foto_perfil VARCHAR(255),  -- Ruta o URL de la foto de perfil
    descripcion TEXT,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    banner_imagen VARCHAR(255),
    redes_sociales JSON  -- Ejemplo: {"linkedin": "url", "github": "url"}
);

-- Tabla de experiencia laboral
CREATE TABLE IF NOT EXISTS experiencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    puesto VARCHAR(100) NOT NULL,
    empresa VARCHAR(100) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT,
    es_actual BOOLEAN DEFAULT FALSE
);

-- Tabla de educación
CREATE TABLE IF NOT EXISTS educacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instituto VARCHAR(100) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT
);

-- Tabla de habilidades
CREATE TABLE IF NOT EXISTS habilidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    porcentaje INT,  -- Para habilidades técnicas (ej: 80%)
    tipo VARCHAR(50)  -- Ejemplo: "Técnica", "Blanda"
);

-- Tabla de proyectos
CREATE TABLE IF NOT EXISTS proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha DATE,
    enlace VARCHAR(255),
    imagen VARCHAR(255)
);
USE portafolio_db;


select * from datos_personales;
INSERT INTO datos_personales (
    nombre,
    titulo,
    foto_perfil,
    descripcion,
    email,
    telefono,
    direccion,
    redes_sociales,
    banner_imagen
) VALUES (
    'Joaco Fritz',
    'Full Stack Developer Jr.',
    'static/images/joaco_fritz.jpg',  -- Ruta relativa a la carpeta static
    'Soy un desarrollador full stack con experiencia en Python, Flask, y bases de datos SQL. Apasionado por crear soluciones innovadoras y funcionales.',
    'joaco.fritz@example.com',
    '+54 11 1234-5678',
    'Buenos Aires, Argentina',
    '{"linkedin": "https://www.linkedin.com/in/ztirfj-fritz-carrizo-51661b398/", "github": "https://github.com/JoaquinFritz16"}',
    'images/banner-bg.jpg'  -- Ruta relativa a la carpeta static
);

ALTER TABLE usuarios ADD COLUMN es_admin BOOLEAN DEFAULT FALSE;
INSERT INTO usuarios (username, password, es_admin) VALUES ('Admin', 'contraseña_segura', TRUE);


select * from datos_personales;
select * from usuarios;
SELECT * FROM usuarios WHERE username = 'Admin';
UPDATE usuarios SET password = 'scrypt:32768:8:1$UeIpy3hmzCyDp8rY$2d2ae3a3c44e551e0d012632dea7cbaea1fbb46e3f878929787f4c1cb25da4b5fa6e001146041f774103152a893c1542be4a405d2ef890d6946527694d5d98ee' WHERE username = 'Admin';
INSERT INTO experiencia (puesto, empresa, fecha_inicio, fecha_fin, descripcion, es_actual)
VALUES
('Desarrollador Full Stack Jr.', 'Tech Solutions', '2023-01-15', '2024-06-30', 'Desarrollo de aplicaciones web con Flask y SQLAlchemy. Participación en proyectos de migración de bases de datos.', FALSE),
('Pasante de Desarrollo', 'Innovatech', '2022-05-01', '2022-12-31', 'Apoyo en el desarrollo de APIs RESTful y mantenimiento de bases de datos MySQL.', FALSE);

INSERT INTO educacion (instituto, titulo, fecha_inicio, fecha_fin, descripcion)
VALUES
('Instituto Técnico Renault', 'Técnico en Programación', '2020-03-01', '2022-12-15', 'Formación en desarrollo de software y bases de datos.'),
('Universidad Nacional', 'Ingeniería en Sistemas (en curso)', '2023-03-01', NULL, 'Cursando materias relacionadas con desarrollo web y bases de datos.');
INSERT INTO educacion (instituto, titulo, fecha_inicio, fecha_fin, descripcion)
VALUES
('Instituto Técnico Renault', 'Técnico en Programación', '2020-03-01', '2022-12-15', 'Formación en desarrollo de software y bases de datos.'),
('Universidad Nacional', 'Ingeniería en Sistemas (en curso)', '2023-03-01', NULL, 'Cursando materias relacionadas con desarrollo web y bases de datos.');

INSERT INTO habilidades (nombre, porcentaje, tipo)
VALUES
('Python', 90, 'Técnica'),
('Flask', 85, 'Técnica'),
('SQL', 80, 'Técnica'),
('JavaScript', 75, 'Técnica'),
('Trabajo en Equipo', 95, 'Blanda'),
('Comunicación', 90, 'Blanda');

