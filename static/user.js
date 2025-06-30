// Manejo del panel de usuario

document.addEventListener('DOMContentLoaded', function () {
    // Verificar autenticación
    const token = localStorage.getItem('access_token');
    if (!token && window.location.pathname !== '/login' && window.location.pathname !== '/register') {
        window.location.href = '/login';
        return;
    }

    // Cargar datos del usuario
    if (document.getElementById('edit-profile-form')) {
        loadUserData();
    }

    // Manejar formulario de edición de perfil
    const editProfileForm = document.getElementById('edit-profile-form');
    if (editProfileForm) {
        editProfileForm.addEventListener('submit', handleEditProfile);
    }

    // Manejar cambio de contraseña
    const changePasswordForm = document.getElementById('change-password-form');
    if (changePasswordForm) {
        changePasswordForm.addEventListener('submit', handleChangePassword);
    }
});

async function loadUserData() {
    try {
        const response = await fetch('/usuarios/me', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });

        if (!response.ok) {
            throw new Error('Error al cargar datos del usuario');
        }

        const user = await response.json();

        // Llenar formulario de edición
        document.getElementById('edit-nombre').value = user.nombre_completo;
        document.getElementById('edit-edad').value = user.edad || '';
        document.getElementById('edit-imagen').value = user.imagen || '';

        // Cargar facultades y seleccionar la del usuario
        const facultadSelect = document.getElementById('edit-facultad');
        const facultadesResponse = await fetch('/facultades/');
        const facultades = await facultadesResponse.json();

        facultadSelect.innerHTML = '<option value="">Seleccione una facultad</option>';
        facultades.forEach(facultad => {
            const option = document.createElement('option');
            option.value = facultad.id;
            option.textContent = facultad.nombre;
            facultadSelect.appendChild(option);
        });

        if (user.carrera) {
            facultadSelect.value = user.carrera.facultad_id;

            // Cargar carreras de la facultad
            const carreraSelect = document.getElementById('edit-carrera');
            const carrerasResponse = await fetch(`/carreras/?facultad_id=${user.carrera.facultad_id}`);
            const carreras = await carrerasResponse.json();

            carreraSelect.innerHTML = '<option value="">Seleccione una carrera</option>';
            carreras.forEach(carrera => {
                const option = document.createElement('option');
                option.value = carrera.id;
                option.textContent = carrera.nombre;
                carreraSelect.appendChild(option);
            });

            carreraSelect.value = user.carrera_id;
        }

        // Cargar géneros y seleccionar el del usuario
        const generoSelect = document.getElementById('edit-genero');
        const generosResponse = await fetch('/generos/');
        const generos = await generosResponse.json();

        generoSelect.innerHTML = '<option value="">Seleccione un género</option>';
        generos.forEach(genero => {
            const option = document.createElement('option');
            option.value = genero.id;
            option.textContent = genero.nombre;
            generoSelect.appendChild(option);
        });

        if (user.genero_id) {
            generoSelect.value = user.genero_id;
        }

        // Manejar cambio de facultad
        facultadSelect.addEventListener('change', async function () {
            const carreraSelect = document.getElementById('edit-carrera');
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
            }
        });
    } catch (error) {
        console.error('Error al cargar datos del usuario:', error);
    }
}

async function handleEditProfile(e) {
    e.preventDefault();

    const errorElement = document.getElementById('edit-profile-error');
    const successElement = document.getElementById('edit-profile-success');

    const formData = {
        nombre_completo: document.getElementById('edit-nombre').value,
        edad: document.getElementById('edit-edad').value ? parseInt(document.getElementById('edit-edad').value) : null,
        carrera_id: parseInt(document.getElementById('edit-carrera').value),
        genero_id: parseInt(document.getElementById('edit-genero').value),
        imagen: document.getElementById('edit-imagen').value || null
    };

    try {
        const response = await fetch('/usuarios/me', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Error al actualizar perfil');
        }

        const updatedUser = await response.json();

        // Actualizar la UI
        document.getElementById('user-name').textContent = updatedUser.nombre_completo;
        document.getElementById('user-edad').textContent = updatedUser.edad || 'No especificada';
        document.getElementById('user-carrera').textContent = updatedUser.carrera?.nombre || 'No especificada';
        document.getElementById('user-facultad').textContent = updatedUser.carrera?.facultad.nombre || 'No especificada';
        document.getElementById('user-genero').textContent = updatedUser.genero?.nombre || 'No especificado';
        document.getElementById('user-avatar').src = updatedUser.imagen || '/static/images/default-avatar.png';

        // Mostrar mensaje de éxito
        errorElement.classList.add('d-none');
        successElement.textContent = 'Perfil actualizado correctamente';
        successElement.classList.remove('d-none');

        // Ocultar mensaje después de 3 segundos
        setTimeout(() => {
            successElement.classList.add('d-none');
        }, 3000);
    } catch (error) {
        errorElement.textContent = error.message;
        errorElement.classList.remove('d-none');
        successElement.classList.add('d-none');
    }
}

async function handleChangePassword(e) {
    e.preventDefault();

    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    const errorElement = document.getElementById('change-password-error');
    const successElement = document.getElementById('change-password-success');

    try {
        if (newPassword !== confirmPassword) {
            throw new Error('Las contraseñas no coinciden');
        }

        const response = await fetch('/usuarios/me/password', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify({
                current_password: currentPassword,
                new_password: newPassword
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Error al cambiar contraseña');
        }

        // Mostrar mensaje de éxito
        errorElement.classList.add('d-none');
        successElement.textContent = 'Contraseña cambiada correctamente';
        successElement.classList.remove('d-none');
        document.getElementById('change-password-form').reset();

        // Ocultar mensaje después de 3 segundos
        setTimeout(() => {
            successElement.classList.add('d-none');
        }, 3000);
    } catch (error) {
        errorElement.textContent = error.message;
        errorElement.classList.remove('d-none');
        successElement.classList.add('d-none');
    }
}