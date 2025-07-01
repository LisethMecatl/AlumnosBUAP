<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= htmlspecialchars($title) ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/AlumnosBUAP/front/static/css/styles.css">
</head>

<body>
    <?php include 'header.php'; ?>

    <div class="container mt-4">
        <?php include $content; ?>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <?php foreach ($scripts as $script): ?>
        <script src="/AlumnosBUAP/front/static/js/<?= htmlspecialchars($script) ?>.js"></script>
    <?php endforeach; ?>
</body>

</html>