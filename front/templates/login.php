<?php require_once '../includes/config.php'; ?>

<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
    <link href="../static/css/styles.css" rel="stylesheet">
</head>

<body>
    <div class="container">
        <h1 class="login-title">Bienvenido</h1>
        <form id="login-form" action="auth.php?action=login" method="POST">
            <input type="text" name="matricula" placeholder="Matrícula" required>
            <input type="password" name="contrasena" placeholder="Contraseña" required>
            <button type="submit">Iniciar Sesión</button>
        </form>
        <a href="register.php" class="register-btn">Registrarse</a>
        <?php if (isset($_SESSION['error'])): ?>
            <div class="alert alert-danger"><?= $_SESSION['error'] ?></div>
            <?php unset($_SESSION['error']); ?>
        <?php endif; ?>
    </div>
    <script src="/static/js/auth.js"></script>
</body>

</html>