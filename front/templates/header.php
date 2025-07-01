<?php if (isset($_SESSION['jwt_token'])): ?>
    <nav>
        <a href="dashboard.php">Inicio</a>
        <?php if ($_SESSION['acceso_id'] == 1): ?>
            <a href="admin.php">Admin</a>
        <?php endif; ?>
        <a href="auth.php?action=logout">Salir</a>
    </nav>
<?php endif; ?>