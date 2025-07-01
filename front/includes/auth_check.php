<?php
require_once 'config.php';

function check_auth()
{
    if (!isset($_SESSION['jwt_token'])) {
        header('Location: login.php');
        exit();
    }
}

function check_admin()
{
    check_auth();
    // Verificar rol de admin (necesitarías un endpoint en tu API)
    $user = api_request('/usuarios/me');
    if ($user['acceso_id'] !== 1) {
        header('Location: dashboard.php');
        exit();
    }
}
