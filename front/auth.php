<?php
require_once 'includes/config.php';
session_start();

$action = $_GET['action'] ?? '';

if ($action === 'login') {
    $data = [
        'username' => $_POST['matricula'],
        'password' => $_POST['contrasena']
    ];

    $response = api_request('/login', 'POST', $data);

    if (isset($response['access_token'])) {
        $_SESSION['jwt_token'] = $response['access_token'];
        // Obtener datos del usuario
        $user = api_request('/usuarios/me', 'GET');
        $_SESSION['user_data'] = $user;
        header('Location: dashboard.php');
    } else {
        $_SESSION['error'] = $response['detail'] ?? 'Credenciales incorrectas';
        header('Location: login.php');
    }
    exit();
}
