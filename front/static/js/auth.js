// Puedes mantenerlo para AJAX, pero ahora con endpoints PHP
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const response = await fetch('auth.php?action=login', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        window.location.href = 'dashboard.php';
    } else {
        alert('Error en el login');
    }
});