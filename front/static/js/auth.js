document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        username: e.target.matricula.value,
        password: e.target.contrasena.value
    };

    try {
        const response = await fetch('/AlumnosBUAP/front/includes/auth.php?action=login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.redirected) {
            window.location.href = response.url;
        } else {
            const result = await response.json();
            if (result.error) {
                alert(result.message || 'Error en el login');
            }
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error de conexión con el servidor');
    }
});