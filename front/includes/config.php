<?php
define('API_URL', 'http://localhost:8000'); // Asegúrate que coincide con tu FastAPI
session_start();

function api_request($endpoint, $method = 'GET', $data = null)
{
    $url = API_URL . $endpoint;
    $headers = ['Content-Type: application/json'];

    if (isset($_SESSION['jwt_token'])) {
        $headers[] = 'Authorization: Bearer ' . $_SESSION['jwt_token'];
    }

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST => $method,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => $headers,
        CURLOPT_POSTFIELDS => $data ? json_encode($data) : null
    ]);

    $response = curl_exec($ch);
    return json_decode($response, true) ?: [];
}
