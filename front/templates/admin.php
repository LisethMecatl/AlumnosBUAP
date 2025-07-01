{% extends "base.html" %}

{% block title %}Administración{% endblock %}

{% block content %}
<div class="container-fluid">
    <h2 class="mb-4">Panel de Administración</h2>

    <ul class="nav nav-tabs" id="adminTabs" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="usuarios-tab" data-bs-toggle="tab" data-bs-target="#usuarios"
                type="button">Usuarios</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="facultades-tab" data-bs-toggle="tab" data-bs-target="#facultades"
                type="button">Facultades</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="carreras-tab" data-bs-toggle="tab" data-bs-target="#carreras"
                type="button">Carreras</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="preferencias-tab" data-bs-toggle="tab" data-bs-target="#preferencias"
                type="button">Preferencias</button>
        </li>
    </ul>

    <div class="tab-content p-3 border border-top-0 rounded-bottom" id="adminTabsContent">
        <!-- Tab Usuarios -->
        <div class="tab-pane fade show active" id="usuarios" role="tabpanel">
            <div class="d-flex justify-content-between mb-3">
                <h4>Gestión de Usuarios</h4>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addUserModal">Agregar
                    Usuario</button>
            </div>

            <div class="table-responsive">
                <table class="table table-striped table-hover" id="users-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Matrícula</th>
                            <th>Edad</th>
                            <th>Carrera</th>
                            <th>Acceso</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Datos se cargarán con JavaScript -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Tab Facultades -->
        <div class="tab-pane fade" id="facultades" role="tabpanel">
            <div class="d-flex justify-content-between mb-3">
                <h4>Gestión de Facultades</h4>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addFacultadModal">Agregar
                    Facultad</button>
            </div>

            <div class="table-responsive">
                <table class="table table-striped table-hover" id="facultades-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Datos se cargarán con JavaScript -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Tab Carreras -->
        <div class="tab-pane fade" id="carreras" role="tabpanel">
            <div class="d-flex justify-content-between mb-3">
                <h4>Gestión de Carreras</h4>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addCarreraModal">Agregar
                    Carrera</button>
            </div>

            <div class="table-responsive">
                <table class="table table-striped table-hover" id="carreras-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Facultad</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Datos se cargarán con JavaScript -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Tab Preferencias -->
        <div class="tab-pane fade" id="preferencias" role="tabpanel">
            <ul class="nav nav-pills mb-3" id="preferencias-tabs" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="deportes-tab" data-bs-toggle="pill" data-bs-target="#deportes"
                        type="button">Deportes</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="peliculas-tab" data-bs-toggle="pill" data-bs-target="#peliculas"
                        type="button">Películas</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="hobbies-tab" data-bs-toggle="pill" data-bs-target="#hobbies"
                        type="button">Hobbies</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="colores-tab" data-bs-toggle="pill" data-bs-target="#colores"
                        type="button">Colores</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="musicas-tab" data-bs-toggle="pill" data-bs-target="#musicas"
                        type="button">Música</button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="generos-tab" data-bs-toggle="pill" data-bs-target="#generos"
                        type="button">Géneros</button>
                </li>
            </ul>

            <div class="tab-content" id="preferencias-tabs-content">
                <!-- Deportes -->
                <div class="tab-pane fade show active" id="deportes" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Deportes</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addDeporteModal">Agregar Deporte</button>
                    </div>
                    <table class="table table-striped table-hover" id="deportes-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>

                <!-- Películas -->
                <div class="tab-pane fade" id="peliculas" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Películas</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addPeliculaModal">Agregar Película</button>
                    </div>
                    <table class="table table-striped table-hover" id="peliculas-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Título</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>

                <!-- Hobbies -->
                <div class="tab-pane fade" id="hobbies" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Hobbies</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addHobbyModal">Agregar Hobby</button>
                    </div>
                    <table class="table table-striped table-hover" id="hobbies-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>

                <!-- Colores -->
                <div class="tab-pane fade" id="colores" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Colores</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addColorModal">Agregar Color</button>
                    </div>
                    <table class="table table-striped table-hover" id="colores-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>

                <!-- Música -->
                <div class="tab-pane fade" id="musicas" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Géneros Musicales</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addMusicaModal">Agregar Género</button>
                    </div>
                    <table class="table table-striped table-hover" id="musicas-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Género</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>

                <!-- Géneros -->
                <div class="tab-pane fade" id="generos" role="tabpanel">
                    <div class="d-flex justify-content-between mb-3">
                        <h5>Géneros</h5>
                        <button class="btn btn-primary btn-sm" data-bs-toggle="modal"
                            data-bs-target="#addGeneroModal">Agregar Género</button>
                    </div>
                    <table class="table table-striped table-hover" id="generos-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Datos se cargarán con JavaScript -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal Agregar Usuario -->
<div class="modal fade" id="addUserModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Agregar Usuario</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form id="add-user-form">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="admin-nombre" class="form-label">Nombre Completo</label>
                            <input type="text" class="form-control" id="admin-nombre" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="admin-matricula" class="form-label">Matrícula</label>
                            <input type="text" class="form-control" id="admin-matricula" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="admin-edad" class="form-label">Edad</label>
                            <input type="number" class="form-control" id="admin-edad">
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="admin-contrasena" class="form-label">Contraseña</label>
                            <input type="password" class="form-control" id="admin-contrasena" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="admin-facultad" class="form-label">Facultad</label>
                            <select class="form-select" id="admin-facultad" required>
                                <option value="">Seleccione una facultad</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="admin-carrera" class="form-label">Carrera</label>
                            <select class="form-select" id="admin-carrera" required disabled>
                                <option value="">Seleccione una carrera</option>
                            </select>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="admin-genero" class="form-label">Género</label>
                            <select class="form-select" id="admin-genero" required>
                                <option value="">Seleccione un género</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="admin-acceso" class="form-label">Nivel de Acceso</label>
                            <select class="form-select" id="admin-acceso" required>
                                <option value="">Seleccione un nivel</option>
                            </select>
                        </div>
                    </div>

                    <div class="mb-3">
                        <label for="admin-imagen" class="form-label">URL de Imagen (opcional)</label>
                        <input type="text" class="form-control" id="admin-imagen">
                    </div>

                    <div class="alert alert-danger d-none" id="add-user-error"></div>
                    <div class="alert alert-success d-none" id="add-user-success"></div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Guardar Usuario</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Modal Editar Usuario -->
<div class="modal fade" id="editUserModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Editar Usuario</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form id="edit-user-form">
                    <input type="hidden" id="edit-user-id">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-nombre" class="form-label">Nombre Completo</label>
                            <input type="text" class="form-control" id="edit-user-nombre" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-matricula" class="form-label">Matrícula</label>
                            <input type="text" class="form-control" id="edit-user-matricula" required>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-edad" class="form-label">Edad</label>
                            <input type="number" class="form-control" id="edit-user-edad">
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-acceso" class="form-label">Nivel de Acceso</label>
                            <select class="form-select" id="edit-user-acceso" required>
                                <option value="">Seleccione un nivel</option>
                            </select>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-facultad" class="form-label">Facultad</label>
                            <select class="form-select" id="edit-user-facultad" required>
                                <option value="">Seleccione una facultad</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-carrera" class="form-label">Carrera</label>
                            <select class="form-select" id="edit-user-carrera" required>
                                <option value="">Seleccione una carrera</option>
                            </select>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-genero" class="form-label">Género</label>
                            <select class="form-select" id="edit-user-genero" required>
                                <option value="">Seleccione un género</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="edit-user-imagen" class="form-label">URL de Imagen</label>
                            <input type="text" class="form-control" id="edit-user-imagen">
                        </div>
                    </div>

                    <div class="alert alert-danger d-none" id="edit-user-error"></div>
                    <div class="alert alert-success d-none" id="edit-user-success"></div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Modal Confirmar Eliminación -->
<div class="modal fade" id="confirmDeleteModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Confirmar Eliminación</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p id="delete-message">¿Estás seguro de que deseas eliminar este elemento?</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                <button type="button" class="btn btn-danger" id="confirm-delete-btn">Eliminar</button>
            </div>
        </div>
    </div>
</div>

<!-- Modales para agregar otros elementos (facultades, carreras, etc.) -->
<!-- Se implementarían de manera similar a los modales anteriores -->

{% block scripts %}
<script src="/static/js/admin.js"></script>
{% endblock %}
{% endblock %}