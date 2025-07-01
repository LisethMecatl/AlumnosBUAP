<?php
session_start();

//define('BASE_PATH', __DIR__ . '/../');
//define('BASE_URL', '/AlumnosBUAP/front/');

// Configuración de la API
define('API_BASE_URL', 'http://localhost:8000'); // Asegúrate que el puerto sea correcto

// Verifica que CURL esté configurado correctamente
function api_request($endpoint, $method = 'GET', $data = null)
{
    $url = API_BASE_URL . $endpoint;
    $headers = ['Content-Type: application/json'];

    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CUSTOMREQUEST => $method,
        CURLOPT_HTTPHEADER => $headers,
        CURLOPT_POSTFIELDS => $data ? json_encode($data) : null,
        CURLOPT_FOLLOWLOCATION => false,
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if (curl_errno($ch)) {
        $error = curl_error($ch);
        curl_close($ch);
        return ['status' => 500, 'data' => ['detail' => $error]];
    }

    curl_close($ch);

    return [
        'status' => $httpCode,
        'data' => json_decode($response, true) ?: []
    ];
}
