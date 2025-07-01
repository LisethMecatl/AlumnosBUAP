<?php
require_once 'config.php';

function check_auth()
{
    if (!isset($_SESSION['jwt_token'])) {
        header('Location: ' . BASE_URL . '?page=login');
        exit();
    }

    $response = api_request('/usuarios/me');

    if ($response['status'] !== 200) {
        session_destroy();
        header('Location: ' . BASE_URL . '?page=login');
        exit();
    }

    $_SESSION['user'] = $response['data'];
}

function check_admin()
{
    check_auth();

    if ($_SESSION['user']['acceso_id'] !== 1) {
        header('Location: ' . BASE_URL . '?page=dashboard');
        exit();
    }
}
