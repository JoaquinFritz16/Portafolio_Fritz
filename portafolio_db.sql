-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS portafolio_db;
USE portafolio_db;

-- Tabla de usuarios (login)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    es_admin BOOLEAN DEFAULT FALSE
);

-- Tabla de datos personales
CREATE TABLE IF NOT EXISTS datos_personales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    titulo VARCHAR(100),
    foto_perfil VARCHAR(255),
    descripcion TEXT,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    banner_imagen VARCHAR(255),
    redes_sociales JSON
);

-- Tabla experiencia laboral
CREATE TABLE IF NOT EXISTS experiencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    puesto VARCHAR(100) NOT NULL,
    empresa VARCHAR(100) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT,
    es_actual BOOLEAN DEFAULT FALSE
);

-- Tabla educación
CREATE TABLE IF NOT EXISTS educacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instituto VARCHAR(100) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT
);

-- Tabla habilidades
CREATE TABLE IF NOT EXISTS habilidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    porcentaje INT,
    tipo VARCHAR(50)
);

-- Tabla proyectos
CREATE TABLE IF NOT EXISTS proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha DATE,
    enlace VARCHAR(255),
    imagen VARCHAR(255)
);

-- Insert datos personales
INSERT INTO datos_personales (
    nombre, titulo, foto_perfil, descripcion, email, telefono,
    direccion, redes_sociales, banner_imagen
) VALUES (
    'Joaco Fritz',
    'Full Stack Developer Jr.',
    'static/images/joaco_fritz.jpg',
    'Soy un desarrollador full stack con experiencia en Python, Flask, y bases de datos SQL. Apasionado por crear soluciones innovadoras y funcionales.',
    'joaco.fritz@example.com',
    '+54 11 1234-5678',
    'Buenos Aires, Argentina',
    '{"linkedin": "https://www.linkedin.com/in/ztirfj-fritz-carrizo-51661b398/", "github": "https://github.com/JoaquinFritz16"}',
    'images/banner-bg.jpg'
);

-- Crear usuario Admin con password hasheada
INSERT INTO usuarios (username, password, es_admin)
VALUES (
    'Admin',
    'scrypt:32768:8:1$eQoacv8su8zWyGJk$8c5023f89cb697c4f84823679b15907c3ba52af5dfddf4dff68c7a5dd1eb64bba305c58aed83a316a454b49cc9c1ebda537d8ae403763ce6c2ea1787784b7c48',
    TRUE
);

-- Experiencia
INSERT INTO experiencia (puesto, empresa, fecha_inicio, fecha_fin, descripcion, es_actual)
VALUES
('Desarrollador Full Stack Jr.', 'Tech Solutions', '2023-01-15', '2024-06-30',
 'Desarrollo de aplicaciones web con Flask y SQLAlchemy. Participación en proyectos de migración de bases de datos.', FALSE),
('Pasante de Desarrollo', 'Innovatech', '2022-05-01', '2022-12-31',
 'Apoyo en el desarrollo de APIs RESTful y mantenimiento de bases de datos MySQL.', FALSE);

-- Educación
INSERT INTO educacion (instituto, titulo, fecha_inicio, fecha_fin, descripcion)
VALUES
('Instituto Técnico Renault', 'Técnico en Programación', '2020-03-01', '2022-12-15',
 'Formación en desarrollo de software y bases de datos.'),
('Universidad Nacional', 'Ingeniería en Sistemas (en curso)', '2023-03-01', NULL,
 'Cursando materias relacionadas con desarrollo web y bases de datos.');

-- Habilidades
INSERT INTO habilidades (nombre, porcentaje, tipo)
VALUES
('Python', 90, 'Técnica'),
('Flask', 85, 'Técnica'),
('SQL', 80, 'Técnica'),
('JavaScript', 75, 'Técnica'),
('Trabajo en Equipo', 95, 'Blanda'),
('Comunicación', 90, 'Blanda');
SELECT * FROM experiencia;
SELECT * FROM educacion;
SELECT * FROM proyectos;
ALTER TABLE habilidades ADD COLUMN icono VARCHAR(255);

SELECT * FROM habilidades;
select * from usuarios;
UPDATE usuarios
SET password = 'scrypt:32768:8:1$T30qTFZ9ta2XmBFV$47f0e804d9a1379b8bd3869e47313f41a3985712c8723bcf188e9d922884cfda990bbdefd4ba3e6a5f008fa950a0c9c06cf0bf16596c722329d48fcc15cec938'
WHERE username = 'Admin';
DESCRIBE experiencia;
select * from experiencia;
DESCRIBE datos_personales;
UPDATE datos_personales SET foto_perfil = 'images/joaco_fritz.jpg' WHERE id = 1;

