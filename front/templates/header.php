<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="/">Alumnos BUAP</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <?php if (!isset($_SESSION['user'])): ?>
                    <li class="nav-item">
                        <a class="nav-link" href="login.php">Iniciar Sesión</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="register.php">Registrarse</a>
                    </li>
                <?php else: ?>
                    <li class="nav-item">
                        <a class="nav-link" href="dashboard.php">Panel</a>
                    </li>
                    <?php if ($_SESSION['user']['acceso_id'] == 1): ?>
                        <li class="nav-item">
                            <a class="nav-link" href="admin.php">Administración</a>
                        </li>
                    <?php endif; ?>
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">Cerrar Sesión</a>
                    </li>
                <?php endif; ?>
            </ul>
        </div>
    </div>
</nav>