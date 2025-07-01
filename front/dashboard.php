<?php
require_once 'includes/auth_check.php';
$user = api_request('/usuarios/me');
?>

<?php include 'templates/header.php'; ?>

<div class="container">
    <h1>Bienvenido, <?= htmlspecialchars($user['nombre_completo']) ?></h1>

    <!-- Mostrar datos académicos -->
    <div class="card">
        <div class="card-body">
            <h5>Carrera: <?= $user['carrera']['nombre'] ?? 'No especificada' ?></h5>
            <p>Facultad: <?= $user['carrera']['facultad']['nombre'] ?? 'No especificada' ?></p>
        </div>
    </div>
</div>