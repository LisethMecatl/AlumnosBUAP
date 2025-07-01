// Manejo del panel de administración

document.addEventListener('DOMContentLoaded', function () {
    // Verificar autenticación y permisos
    const token = localStorage.getItem('access_token');
    if (!token) {
        window.location.href = '/login';
        return;
    }

    // Verificar si es admin
    verifyAdmin();

    // Cargar datos según la pestaña activa
    const activeTab = document.querySelector('.nav-link.active');
    if (activeTab) {
        loadTabData(activeTab.id.replace('-tab', ''));
    }

    // Manejar cambio de pestañas
    const tabLinks = document.querySelectorAll('.nav-link[data-bs-toggle="tab"]');
    tabLinks.forEach(link => {
        link.addEventListener('shown.bs.tab', function (e) {
            loadTabData(e.target.id.replace('-tab', ''));
        });
    });

    // Manejar formularios y botones
    setupAdminForms();
});

async function verifyAdmin() {
    try {
        const response = await fetch('/usuarios/me', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });

        if (!response.ok) {
            throw new Error('Error al verificar permisos');
        }

        const user = await response.json();
        if (user.acceso_id !== 1) {
            window.location.href = '/dashboard';
        }
    } catch (error) {
        console.error('Error al verificar permisos:', error);
        window.location.href = '/';
    }
}

async function loadTabData(tabName) {
    switch (tabName) {
        case 'usuarios':
            await loadUsers();
            break;
        case 'facultades':
            await loadFacultades();
            break;
        case 'carreras':
            await loadCarreras();
            break;
        case 'deportes':
            await loadDeportes();
            break;
        case 'peliculas':
            await loadPeliculas();
            break;
        case 'hobbies':
            await loadHobbies();
            break;
        case 'colores':
            await loadColores();
            break;
        case 'musicas':
            await loadMusicas();
            break;
        case 'generos':
            await loadGeneros();
            break;
    }
}

async function loadUsers() {
    try {
        const response = await fetch('/usuarios/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });

        if (!response.ok) {
            throw new Error('Error al cargar usuarios');
        }

        const users = await response.json();
        const tableBody = document.querySelector('#users-table tbody');
        tableBody.innerHTML = '';

        users.forEach(user => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.nombre_completo}</td>
                <td>${user.matricula}</td>
                <td>${user.edad || '-'}</td>
                <td>${user.carrera?.nombre || '-'}</td>
                <td>${user.acceso?.nivel || '-'}</td>
                <td>
                    <button class="btn btn-sm btn-primary edit-user" data-id="${user.id}">Editar</button>
                    <button class="btn btn-sm btn-danger delete-user" data-id="${user.id}">Eliminar</button>
                </td>
            `;

            tableBody.appendChild(row);
        });

        // Agregar event listeners a los botones
        document.querySelectorAll('.edit-user').forEach(btn => {
            btn.addEventListener('click', () => openEditUserModal(btn.dataset.id));
        });

        document.querySelectorAll('.delete-user').forEach(btn => {
            btn.addEventListener('click', () => confirmDelete('usuario', btn.dataset.id));
        });
    } catch (error) {
        console.error('Error al cargar usuarios:', error);
    }
}

async function openEditUserModal(userId) {
    try {
        // Cargar datos del usuario
        const userResponse = await fetch(`/usuarios/${userId}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });

        if (!userResponse.ok) {
            throw new Error('Error al cargar datos del usuario');
        }

        const user = await userResponse.json();

        // Llenar formulario
        document.getElementById('edit-user-id').value = user.id;
        document.getElementById('edit-user-nombre').value = user.nombre_completo;
        document.getElementById('edit-user-matricula').value = user.matricula;
        document.getElementById('edit-user-edad').value = user.edad || '';
        document.getElementById('edit-user-imagen').value = user.imagen || '';

        // Cargar facultades y seleccionar la del usuario
        const facultadSelect = document.getElementById('edit-user-facultad');
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
            const carreraSelect = document.getElementById('edit-user-carrera');
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
        const generoSelect = document.getElementById('edit-user-genero');
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

        // Cargar niveles de acceso y seleccionar el del usuario
        const accesoSelect = document.getElementById('edit-user-acceso');
        const accesosResponse = await fetch('/accesos/');
        const accesos = await accesosResponse.json();

        accesoSelect.innerHTML = '<option value="">Seleccione un nivel</option>';
        accesos.forEach(acceso => {
            const option = document.createElement('option');
            option.value = acceso.id;
            option.textContent = acceso.nivel;
            accesoSelect.appendChild(option);
        });

        if (user.acceso_id) {
            accesoSelect.value = user.acceso_id;
        }

        // Mostrar modal
        const modal = new bootstrap.Modal(document.getElementById('editUserModal'));
        modal.show();
    } catch (error) {
        console.error('Error al abrir modal de edición:', error);
        alert(error.message);
    }
}

function confirmDelete(type, id) {
    const modal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
    const message = document.getElementById('delete-message');

    message.textContent = `¿Estás seguro de que deseas eliminar este ${type}?`;

    // Configurar botón de confirmación
    const confirmBtn = document.getElementById('confirm-delete-btn');
    confirmBtn.onclick = async function () {
        try {
            let endpoint;
            switch (type) {
                case 'usuario': endpoint = `/usuarios/${id}`; break;
                case 'facultad': endpoint = `/facultades/${id}`; break;
                case 'carrera': endpoint = `/carreras/${id}`; break;
                case 'deporte': endpoint = `/deportes/${id}`; break;
                case 'película': endpoint = `/peliculas/${id}`; break;
                case 'hobby': endpoint = `/hobbies/${id}`; break;
                case 'color': endpoint = `/colores/${id}`; break;
                case 'música': endpoint = `/musicas/${id}`; break;
                case 'género': endpoint = `/generos/${id}`; break;
                default: throw new Error('Tipo no válido');
            }

            const response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                }
            });

            if (!response.ok) {
                throw new Error('Error al eliminar');
            }

            // Recargar datos
            loadTabData(document.querySelector('.nav-link.active').id.replace('-tab', ''));
            modal.hide();
        } catch (error) {
            console.error('Error al eliminar:', error);
            alert(error.message);
        }
    };

    modal.show();
}

// Funciones para cargar otros tipos de datos (facultades, carreras, etc.) seguirían un patrón similar
// Implementaríamos loadFacultades(), loadCarreras(), etc.

function setupAdminForms() {
    // Formulario para agregar usuario
    const addUserForm = document.getElementById('add-user-form');
    if (addUserForm) {
        addUserForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const errorElement = document.getElementById('add-user-error');
            const successElement = document.getElementById('add-user-success');

            const formData = {
                nombre_completo: document.getElementById('admin-nombre').value,
                matricula: document.getElementById('admin-matricula').value,
                edad: document.getElementById('admin-edad').value ? parseInt(document.getElementById('admin-edad').value) : null,
                carrera_id: parseInt(document.getElementById('admin-carrera').value),
                genero_id: parseInt(document.getElementById('admin-genero').value),
                contrasena: document.getElementById('admin-contrasena').value,
                acceso_id: parseInt(document.getElementById('admin-acceso').value),
                imagen: document.getElementById('admin-imagen').value || null
            };

            try {
                const response = await fetch('/usuarios/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    },
                    body: JSON.stringify(formData)
                });

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Error al crear usuario');
                }

                // Mostrar mensaje de éxito
                errorElement.classList.add('d-none');
                successElement.textContent = 'Usuario creado correctamente';
                successElement.classList.remove('d-none');
                addUserForm.reset();

                // Recargar tabla de usuarios
                await loadUsers();

                // Ocultar mensaje después de 3 segundos
                setTimeout(() => {
                    successElement.classList.add('d-none');
                }, 3000);
            } catch (error) {
                errorElement.textContent = error.message;
                errorElement.classList.remove('d-none');
                successElement.classList.add('d-none');
            }
        });

        // Cargar datos para el formulario
        loadAdminFormData();
    }

    // Formulario para editar usuario
    const editUserForm = document.getElementById('edit-user-form');
    if (editUserForm) {
        editUserForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const userId = document.getElementById('edit-user-id').value;
            const errorElement = document.getElementById('edit-user-error');
            const successElement = document.getElementById('edit-user-success');

            const formData = {
                nombre_completo: document.getElementById('edit-user-nombre').value,
                matricula: document.getElementById('edit-user-matricula').value,
                edad: document.getElementById('edit-user-edad').value ? parseInt(document.getElementById('edit-user-edad').value) : null,
                carrera_id: parseInt(document.getElementById('edit-user-carrera').value),
                genero_id: parseInt(document.getElementById('edit-user-genero').value),
                acceso_id: parseInt(document.getElementById('edit-user-acceso').value),
                imagen: document.getElementById('edit-user-imagen').value || null
            };

            try {
                const response = await fetch(`/usuarios/${userId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    },
                    body: JSON.stringify(formData)
                });

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Error al actualizar usuario');
                }

                // Mostrar mensaje de éxito
                errorElement.classList.add('d-none');
                successElement.textContent = 'Usuario actualizado correctamente';
                successElement.classList.remove('d-none');

                // Recargar tabla de usuarios
                await loadUsers();

                // Ocultar mensaje después de 3 segundos
                setTimeout(() => {
                    successElement.classList.add('d-none');
                    bootstrap.Modal.getInstance(document.getElementById('editUserModal')).hide();
                }, 3000);
            } catch (error) {
                errorElement.textContent = error.message;
                errorElement.classList.remove('d-none');
                successElement.classList.add('d-none');
            }
        });
    }
}

async function loadAdminFormData() {
    try {
        // Cargar facultades
        const facultadesResponse = await fetch('/facultades/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        const facultades = await facultadesResponse.json();
        const facultadSelect = document.getElementById('admin-facultad');

        facultadSelect.innerHTML = '<option value="">Seleccione una facultad</option>';
        facultades.forEach(facultad => {
            const option = document.createElement('option');
            option.value = facultad.id;
            option.textContent = facultad.nombre;
            facultadSelect.appendChild(option);
        });

        // Cargar géneros
        const generosResponse = await fetch('/generos/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        const generos = await generosResponse.json();
        const generoSelect = document.getElementById('admin-genero');

        generoSelect.innerHTML = '<option value="">Seleccione un género</option>';
        generos.forEach(genero => {
            const option = document.createElement('option');
            option.value = genero.id;
            option.textContent = genero.nombre;
            generoSelect.appendChild(option);
        });

        // Cargar niveles de acceso
        const accesosResponse = await fetch('/accesos/', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }
        });
        const accesos = await accesosResponse.json();
        const accesoSelect = document.getElementById('admin-acceso');

        accesoSelect.innerHTML = '<option value="">Seleccione un nivel</option>';
        accesos.forEach(acceso => {
            const option = document.createElement('option');
            option.value = acceso.id;
            option.textContent = acceso.nivel;
            accesoSelect.appendChild(option);
        });

        // Habilitar carrera cuando se seleccione facultad
        facultadSelect.addEventListener('change', async function () {
            const carreraSelect = document.getElementById('admin-carrera');
            carreraSelect.innerHTML = '<option value="">Seleccione una carrera</option>';

            if (this.value) {
                const carrerasResponse = await fetch(`/carreras/?facultad_id=${this.value}`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
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