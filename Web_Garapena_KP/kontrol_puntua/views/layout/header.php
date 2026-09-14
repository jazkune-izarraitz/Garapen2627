<?php
/** @var array $lang */
/** @var string $currentLang */
/** @var array $availableLanguages */
/** @var array|null $flash */
/** @var string $baseUrl */
?>
<!DOCTYPE html>
<html lang="<?php echo htmlspecialchars($currentLang, ENT_QUOTES, 'UTF-8'); ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?php echo htmlspecialchars($lang['title'], ENT_QUOTES, 'UTF-8'); ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/css/styles.css" rel="stylesheet">
</head>
<body class="app-body">
<!-- Goiko nabigazio barra: ekintza azkarrak eta hizkuntza hautatzailea -->
<nav class="navbar navbar-expand-lg navbar-dark main-nav">
    <div class="container-fluid">
        <a class="navbar-brand" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php">
            <?php echo htmlspecialchars($lang['title'], ENT_QUOTES, 'UTF-8'); ?>
        </a>
        <div class="d-flex align-items-center gap-3">
            <a class="btn btn-accent btn-sm" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=create">
                <?php echo htmlspecialchars($lang['add_student'], ENT_QUOTES, 'UTF-8'); ?>
            </a>
            <a class="btn btn-outline-light btn-sm" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=logs">
                <?php echo htmlspecialchars($lang['view_logs'], ENT_QUOTES, 'UTF-8'); ?>
            </a>
            <form method="get" action="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php" class="d-flex align-items-center text-white">
                <label for="langSelector" class="me-2 mb-0 small fw-semibold">
                    <?php echo htmlspecialchars($lang['language_label'], ENT_QUOTES, 'UTF-8'); ?>
                </label>
                <select class="form-select form-select-sm lang-select" id="langSelector" name="lang" onchange="this.form.submit()">
                    <?php foreach ($availableLanguages as $code): ?>
                        <option value="<?php echo htmlspecialchars($code, ENT_QUOTES, 'UTF-8'); ?>" <?php echo $code === $currentLang ? 'selected' : ''; ?>>
                            <?php echo strtoupper(htmlspecialchars($code, ENT_QUOTES, 'UTF-8')); ?>
                        </option>
                    <?php endforeach; ?>
                </select>
            </form>
        </div>
    </div>
</nav>
<!-- Eduki nagusia inguratzen duen edukiontzia -->
<div class="container py-4 main-container">
    <?php if (!empty($flash)): ?>
        <!-- Erabiltzaileari feedback bisuala -->
        <div class="alert alert-<?php echo $flash['type'] === 'success' ? 'success' : 'danger'; ?> alert-dismissible fade show alert-flash" role="alert">
            <?php echo htmlspecialchars($flash['message'], ENT_QUOTES, 'UTF-8'); ?>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    <?php endif; ?>
