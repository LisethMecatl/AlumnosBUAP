<?php
require_once __DIR__ . '/config.php';

header('Content-Type: application/json');

$action = $_GET['action'] ?? '';

if ($action === 'login') {
    $json = file_get_contents('php://input');
    $data = json_decode($json, true);

    $response = api_request('/login', 'POST', [
        'username' => $data['username'],
        'password' => $data['password']
    ]);

    if ($response['status'] === 200 && isset($response['data']['access_token'])) {
        $_SESSION['jwt_token'] = $response['data']['access_token'];
        echo json_encode(['success' => true]);
        exit();
    }

    $error = $response['data']['detail'] ?? 'Credenciales incorrectas';
    $_SESSION['error'] = is_array($error) ? implode(', ', $error) : $error;

    echo json_encode([
        'error' => true,
        'message' => $_SESSION['error']
    ]);
    exit();
}
