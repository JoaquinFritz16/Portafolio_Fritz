// Ejemplo de interacción: Mostrar alerta al enviar el formulario de contacto
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('#contacto form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('¡Mensaje enviado! Próximamente me pondré en contacto contigo.');
        });
    }
});
document.addEventListener('DOMContentLoaded', function() {
    // Habilitar drag and drop solo si es admin
    if (window.isAdmin) {
        const sections = document.querySelectorAll('section[id]');
        const container = document.querySelector('main');

        new Sortable(container, {
            animation: 150,
            handle: '.section-handle',  // Clase para el "handle" (icono de arrastrar)
            onEnd: function() {
                // Guardar el nuevo orden en la base de datos
                const newOrder = Array.from(container.children).map(section => section.id);
                fetch('/dashboard/guardar-orden', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ orden: newOrder })
                });
            }
        });
    }
});
// Desplazamiento suave para los enlaces de la navbar
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80, // Ajuste para la navbar fija
                behavior: 'smooth'
            });
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const charts = document.querySelectorAll(".habilidad-chart");

    charts.forEach(canvas => {
        const ctx = canvas.getContext("2d");
        const porcentaje = parseInt(canvas.dataset.porcentaje);
        
        // Asegurar tamaño real del canvas
        const size = canvas.offsetWidth;
        canvas.width = size;
        canvas.height = size;

        const centerX = size / 2;
        const centerY = size / 2;
        const radius = size * 0.35;
        const lineWidth = size * 0.08;

        // -----------------------------------------------
        // 🎨 Selección automática del color según porcentaje
        // -----------------------------------------------
        let colorStart, colorEnd;

        if (porcentaje <= 30) { 
            // ROJO
            colorStart = "#ff7a7a";
            colorEnd = "#ff0000";
        } else if (porcentaje <= 70) { 
            // AMARILLO
            colorStart = "#ffe680";
            colorEnd = "#ffcc00";
        } else {
            // VERDE
            colorStart = "#8df59a";
            colorEnd = "#00cc44";
        }

        // Crear degradado
        const gradient = ctx.createLinearGradient(0, 0, size, size);
        gradient.addColorStop(0, colorStart);
        gradient.addColorStop(1, colorEnd);

        // Animación
        let current = 0;
        const target = porcentaje;

        function animate() {
            ctx.clearRect(0, 0, size, size);

            // Círculo gris de fondo
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.strokeStyle = "#e6e6e6";
            ctx.lineWidth = lineWidth;
            ctx.lineCap = "round";
            ctx.stroke();

            // Círculo de progreso
            const endAngle = (current / 100) * (Math.PI * 2) - Math.PI / 2;
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, -Math.PI / 2, endAngle);
            ctx.strokeStyle = gradient;
            ctx.lineWidth = lineWidth;
            ctx.lineCap = "round";
            ctx.stroke();

            if (current < target) {
                current += 1; // velocidad
                requestAnimationFrame(animate);
            }
        }

        animate();
    });
});

document.querySelectorAll('.eliminar-habilidad').forEach(button => {
    button.addEventListener('click', function() {
        const habilidadId = this.getAttribute('data-id');
        if (confirm('¿Estás seguro de que deseas eliminar esta habilidad?')) {
            fetch(`/dashboard/eliminar-habilidad/${habilidadId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.reload();
                } else {
                    alert('Error al eliminar la habilidad.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});
document.querySelectorAll('.eliminar-experiencia').forEach(button => {
    button.addEventListener('click', function() {
        const experienciaId = this.getAttribute('data-id');
        if (confirm('¿Estás seguro de que deseas eliminar esta experiencia?')) {
            fetch(`/dashboard/eliminar-experiencia/${experienciaId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.reload();
                } else {
                    alert('Error al eliminar la experiencia.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});

document.querySelectorAll('.eliminar-educacion').forEach(button => {
    button.addEventListener('click', function() {
        const educacionId = this.getAttribute('data-id');
        if (confirm('¿Estás seguro de que deseas eliminar esta educación?')) {
            fetch(`/dashboard/eliminar-educacion/${educacionId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.reload();
                } else {
                    alert('Error al eliminar la educación.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});

document.querySelectorAll('.eliminar-proyecto').forEach(button => {
    button.addEventListener('click', function() {
        const proyectoId = this.getAttribute('data-id');
        if (confirm('¿Estás seguro de que deseas eliminar este proyecto?')) {
            fetch(`/dashboard/eliminar-proyecto/${proyectoId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.reload();
                } else {
                    alert('Error al eliminar el proyecto.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});
document.querySelectorAll('.editar-experiencia').forEach(button => {
    button.addEventListener('click', function() {
        const experienciaId = this.getAttribute('data-id');
        fetch(`/dashboard/obtener-experiencia/${experienciaId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('experienciaId').value = data.id;
                document.getElementById('puesto').value = data.puesto;
                document.getElementById('empresa').value = data.empresa;
                document.getElementById('fecha_inicio').value = data.fecha_inicio;
                document.getElementById('fecha_fin').value = data.fecha_fin || '';
                document.getElementById('descripcion').value = data.descripcion;
                document.getElementById('es_actual').checked = data.es_actual;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});

document.querySelectorAll('.editar-habilidad').forEach(button => {
    button.addEventListener('click', function() {
        const habilidadId = this.getAttribute('data-id');
        fetch(`/dashboard/obtener-habilidad/${habilidadId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('habilidadId').value = data.id;
                document.getElementById('nombre').value = data.nombre;
                document.getElementById('porcentaje').value = data.porcentaje;
                document.getElementById('tipo').value = data.tipo;
                document.getElementById('icono').value = data.icono;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
document.querySelectorAll('.editar-proyecto').forEach(button => {
    button.addEventListener('click', function() {
        const proyectoId = this.getAttribute('data-id');
        fetch(`/dashboard/obtener-proyecto/${proyectoId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('proyectoId').value = data.id;
                document.getElementById('nombre').value = data.nombre;
                document.getElementById('descripcion').value = data.descripcion;
                document.getElementById('fecha').value = data.fecha;
                document.getElementById('enlace').value = data.enlace;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
document.querySelectorAll('.editar-educacion').forEach(button => {
    button.addEventListener('click', function() {
        const educacionId = this.getAttribute('data-id');
        fetch(`/dashboard/obtener-educacion/${educacionId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('educacionId').value = data.id;
                document.getElementById('instituto').value = data.instituto;
                document.getElementById('titulo').value = data.titulo;
                document.getElementById('fecha_inicio').value = data.fecha_inicio;
                document.getElementById('fecha_fin').value = data.fecha_fin || '';
                document.getElementById('descripcion').value = data.descripcion;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
