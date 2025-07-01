<?php
// front/index.php
require_once 'includes/config.php';
require_once 'includes/auth_check.php';

$page = $_GET['page'] ?? 'home';

$allowed_pages = [
    'home' => 'templates/index.php',
    'login' => 'templates/login.php',
    'register' => 'templates/register.php',
    'dashboard' => 'templates/dashboard.php',
    'admin' => 'templates/admin.php'
];

if (!array_key_exists($page, $allowed_pages)) {
    $page = 'home';
}

// Verificación de autenticación para páginas protegidas
if (in_array($page, ['dashboard', 'admin']) && !isset($_SESSION['user'])) {
    header('Location: ?page=login');
    exit();
}

if ($page === 'admin') {
    check_admin();
}

// Define las variables para la plantilla base
$title = 'API Alumnos BUAP';
$content = $allowed_pages[$page];
$scripts = []; // Añade aquí los scripts necesarios para cada página

// Incluye la plantilla base
include 'templates/base.php';
