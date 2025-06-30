{% extends "base.html" %}

{% block title %}Panel de Usuario{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-4">
        <div class="card mb-4">
            <div class="card-header">
                <h5>Perfil de Usuario</h5>
            </div>
            <div class="card-body text-center">
                <img src="{{ current_user.imagen or '/static/images/default-avatar.png' }}" class="rounded-circle mb-3"
                    width="150" height="150" id="user-avatar">
                <h4 id="user-name">{{ current_user.nombre_completo }}</h4>
                <p class="text-muted" id="user-matricula">{{ current_user.matricula }}</p>

                <div class="d-grid gap-2">
                    <button class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#editProfileModal">
                        Editar Perfil
                    </button>
                    <button class="btn btn-outline-secondary" data-bs-toggle="modal"
                        data-bs-target="#changePasswordModal">
                        Cambiar Contraseña
                    </button>
                </div>
            </div>
        </div>

        <div class="card mb-4">
            <div class="card-header">
                <h5>Información Académica</h5>
            </div>
            <div class="card-body">
                <p><strong>Facultad:</strong> <span id="user-facultad">{{ current_user.carrera.facultad.nombre if
                        current_user.carrera else 'No especificada' }}</span></p>
                <p><strong>Carrera:</strong> <span id="user-carrera">{{ current_user.carrera.nombre if
                        current_user.carrera else 'No especificada' }}</span></p>
                <p><strong>Edad:</strong> <span id="user-edad">{{ current_user.edad or 'No especificada' }}</span></p>
                <p><strong>Género:</strong> <span id="user-genero">{{ current_user.genero.nombre if current_user.genero
                        else 'No especificado' }}</span></p>
            </div>
        </div>
    </div>

    <div class="col-md-8">
        <div class="card mb-4">
            <div class="card-header">
                <h5>Preferencias</h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <h6>Deportes</h6>
                        <ul class="list-group mb-3" id="user-deportes">
                            {% for deporte in current_user.deportes %}
                            <li class="list-group-item">{{ deporte.nombre }}</li>
                            {% else %}
                            <li class="list-group-item text-muted">No especificados</li>
                            {% endfor %}
                        </ul>

                        <h6>Películas</h6>
                        <ul class="list-group mb-3" id="user-peliculas">
                            {% for pelicula in current_user.peliculas %}
                            <li class="list-group-item">{{ pelicula.titulo }}</li>
                            {% else %}
                            <li class="list-group-item text-muted">No especificadas</li>
                            {% endfor %}
                        </ul>
                    </div>

                    <div class="col-md-6">
                        <h6>Hobbies</h6>
                        <ul class="list-group mb-3" id="user-hobbies">
                            {% for hobby in current_user.hobbies %}
                            <li class="list-group-item">{{ hobby.nombre }}</li>
                            {% else %}
                            <li class="list-group-item text-muted">No especificados</li>
                            {% endfor %}
                        </ul>

                        <h6>Colores</h6>
                        <ul class="list-group mb-3" id="user-colores">
                            {% for color in current_user.colores %}
                            <li class="list-group-item">{{ color.nombre }}</li>
                            {% else %}
                            <li class="list-group-item text-muted">No especificados</li>
                            {% endfor %}
                        </ul>

                        <h6>Música</h6>
                        <ul class="list-group" id="user-musicas">
                            {% for musica in current_user.musicas %}
                            <li class="list-group-item">{{ musica.genero }}</li>
                            {% else %}
                            <li class="list-group-item text-muted">No especificada</li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal Editar Perfil -->
<div class="modal fade" id="editProfileModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Editar Perfil</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form id="edit-profile-form">
                    <div class="mb-3">
                        <label for="edit-nombre" class="form-label">Nombre Completo</label>
                        <input type="text" class="form-control" id="edit-nombre"
                            value="{{ current_user.nombre_completo }}" required>
                    </div>
                    <div class="mb-3">
                        <label for="edit-edad" class="form-label">Edad</label>
                        <input type="number" class="form-control" id="edit-edad" value="{{ current_user.edad or '' }}">
                    </div>
                    <div class="mb-3">
                        <label for="edit-imagen" class="form-label">URL de Imagen</label>
                        <input type="text" class="form-control" id="edit-imagen"
                            value="{{ current_user.imagen or '' }}">
                    </div>
                    <div class="mb-3">
                        <label for="edit-facultad" class="form-label">Facultad</label>
                        <select class="form-select" id="edit-facultad" required>
                            <option value="">Seleccione una facultad</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="edit-carrera" class="form-label">Carrera</label>
                        <select class="form-select" id="edit-carrera" required>
                            <option value="">Seleccione una carrera</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="edit-genero" class="form-label">Género</label>
                        <select class="form-select" id="edit-genero" required>
                            <option value="">Seleccione un género</option>
                        </select>
                    </div>

                    <div class="alert alert-danger d-none" id="edit-profile-error"></div>
                    <div class="alert alert-success d-none" id="edit-profile-success"></div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Modal Cambiar Contraseña -->
<div class="modal fade" id="changePasswordModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Cambiar Contraseña</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <form id="change-password-form">
                    <div class="mb-3">
                        <label for="current-password" class="form-label">Contraseña Actual</label>
                        <input type="password" class="form-control" id="current-password" required>
                    </div>
                    <div class="mb-3">
                        <label for="new-password" class="form-label">Nueva Contraseña</label>
                        <input type="password" class="form-control" id="new-password" required>
                    </div>
                    <div class="mb-3">
                        <label for="confirm-password" class="form-label">Confirmar Nueva Contraseña</label>
                        <input type="password" class="form-control" id="confirm-password" required>
                    </div>

                    <div class="alert alert-danger d-none" id="change-password-error"></div>
                    <div class="alert alert-success d-none" id="change-password-success"></div>

                    <div class="d-grid">
                        <button type="submit" class="btn btn-primary">Cambiar Contraseña</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

{% block scripts %}
<script src="/static/js/user.js"></script>
{% endblock %}
{% endblock %}