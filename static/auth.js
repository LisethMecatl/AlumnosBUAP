// Manejo de autenticación y registro

document.addEventListener('DOMContentLoaded', function () {
    // Login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    // Register
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', handleRegister);
        loadRegisterFormData();
    }

    // Logout
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', handleLogout);
    }
});

async function handleLogin(e) {
    e.preventDefault();

    const matricula = document.getElementById('matricula').value;
    const contrasena = document.getElementById('contrasena').value;
    const errorElement = document.getElementById('login-error');

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                username: matricula,
                password: contrasena,
                grant_type: 'password'
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Error al iniciar sesión');
        }

        const data = await response.json();
        localStorage.setItem('access_token', data.access_token);
        window.location.href = '/dashboard';
    } catch (error) {
        errorElement.textContent = error.message;
        errorElement.classList.remove('d-none');
    }
}

async function handleRegister(e) {
    e.preventDefault();

    const errorElement = document.getElementById('register-error');
    const successElement = document.getElementById('register-success');

    // Obtener todos los valores del formulario
    const formData = {
        nombre_completo: document.getElementById('nombre_completo').value,
        matricula: document.getElementById('matricula').value,
        edad: document.getElementById('edad').value ? parseInt(document.getElementById('edad').value) : null,
        carrera_id: parseInt(document.getElementById('carrera').value),
        genero_id: parseInt(document.getElementById('genero').value),
        contrasena: document.getElementById('contrasena').value,
        acceso_id: 2, // Por defecto usuario normal
        imagen: document.getElementById('imagen').value || null,
        deportes: getSelectedCheckboxes('deportes-container'),
        peliculas: getSelectedCheckboxes('peliculas-container'),
        hobbies: getSelectedCheckboxes('hobbies-container'),
        colores: getSelectedCheckboxes('colores-container'),
        musicas: getSelectedCheckboxes('musicas-container')
    };

    try {
        const response = await fetch('/usuarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Error al registrar usuario');
        }

        // Mostrar mensaje de éxito
        errorElement.classList.add('d-none');
        successElement.classList.remove('d-none');
        document.getElementById('register-form').reset();
    } catch (error) {
        errorElement.textContent = error.message;
        errorElement.classList.remove('d-none');
        successElement.classList.add('d-none');
    }
}

function handleLogout() {
    localStorage.removeItem('access_token');
    window.location.href = '/';
}

async function loadRegisterFormData() {
    try {
        // Cargar facultades
        const facultadesResponse = await fetch('/facultades/');
        const facultades = await facultadesResponse.json();
        const facultadSelect = document.getElementById('facultad');

        facultades.forEach(facultad => {
            const option = document.createElement('option');
            option.value = facultad.id;
            option.textContent = facultad.nombre;
            facultadSelect.appendChild(option);
        });

        // Cargar géneros
        const generosResponse = await fetch('/generos/');
        const generos = await generosResponse.json();
        const generoSelect = document.getElementById('genero');

        generos.forEach(genero => {
            const option = document.createElement('option');
            option.value = genero.id;
            option.textContent = genero.nombre;
            generoSelect.appendChild(option);
        });

        // Cargar preferencias
        await loadPreferences('deportes', 'deportes-container');
        await loadPreferences('peliculas', 'peliculas-container');
        await loadPreferences('hobbies', 'hobbies-container');
        await loadPreferences('colores', 'colores-container');
        await loadPreferences('musicas', 'musicas-container');

        // Habilitar carrera cuando se seleccione facultad
        facultadSelect.addEventListener('change', async function () {
            const carreraSelect = document.getElementById('carrera');
            carreraSelect.innerHTML = '<option value="">Seleccione una carrera</option>';

            if (this.value) {
                const carrerasResponse = await fetch(`/carreras/?facultad_id=${this.value}`);
                const carreras = await carrerasResponse.json();

                carreras.forEach(carrera => {
                    const option = document.createElement('option');
                    option.value = carrera.id;
                    option.textContent = carrera.nombre;
                    carreraSelect.appendChild(option);
                });

                carreraSelect.disabled = false;
            } else {
                carreraSelect.disabled = true;
            }
        });
    } catch (error) {
        console.error('Error al cargar datos del formulario:', error);
    }
}

async function loadPreferences(endpoint, containerId) {
    try {
        const response = await fetch(`/${endpoint}/`);
        const items = await response.json();
        const container = document.getElementById(containerId);

        items.forEach(item => {
            const div = document.createElement('div');
            div.className = 'form-check';

            const input = document.createElement('input');
            input.className = 'form-check-input';
            input.type = 'checkbox';
            input.value = item.id;
            input.id = `${endpoint}-${item.id}`;

            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = input.id;
            label.textContent = item.nombre || item.titulo || item.genero;

            div.appendChild(input);
            div.appendChild(label);
            container.appendChild(div);
        });
    } catch (error) {
        console.error(`Error al cargar ${endpoint}:`, error);
    }
}

function getSelectedCheckboxes(containerId) {
    const container = document.getElementById(containerId);
    const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
    return Array.from(checkboxes).map(checkbox => parseInt(checkbox.value));
}