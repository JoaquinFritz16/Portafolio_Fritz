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
