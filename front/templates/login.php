<?php
require_once __DIR__ . '/../includes/config.php';
require_once __DIR__ . '/../includes/auth_check.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Login</title>
    <link href="/AlumnosBUAP/front/static/css/styles.css" rel="stylesheet">
</head>

<body>
    <div class="container">
        <h1 class="login-title">Bienvenido</h1>
        <form id="login-form" action="/AlumnosBUAP/front/includes/auth.php?action=login" method="POST">
            <input type="text" name="matricula" placeholder="Matrícula" required>
            <input type="password" name="contrasena" placeholder="Contraseña" required>
            <button type="submit">Iniciar Sesión</button>
        </form>
        <a href="?page=register" class="register-btn">Registrarse</a>
        <?php if (isset($_SESSION['error'])): ?>
            <div class="alert alert-danger">
                <?php
                // Asegúrate de mostrar correctamente el error
                if (is_array($_SESSION['error'])) {
                    echo implode('<br>', $_SESSION['error']);
                } else {
                    echo htmlspecialchars($_SESSION['error']);
                }
                ?>
            </div>
            <?php unset($_SESSION['error']); ?>
        <?php endif; ?>
    </div>
    <script src="/AlumnosBUAP/front/static/js/auth.js"></script>
</body>

</html>