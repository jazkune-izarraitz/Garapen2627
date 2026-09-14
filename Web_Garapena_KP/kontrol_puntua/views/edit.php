<?php require __DIR__ . '/layout/header.php'; ?>
<!-- Dagoen ikaslea editatzeko formularioa -->
<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card form-card shadow-lg">
            <div class="card-header bg-white">
                <h5 class="mb-0"><?php echo htmlspecialchars($lang['edit'], ENT_QUOTES, 'UTF-8'); ?></h5>
            </div>
            <div class="card-body">
                <!-- Datu baliogarrien formulario eguneratua -->
                <form method="post" action="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=update" enctype="multipart/form-data" id="editForm">
                    <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($csrfToken, ENT_QUOTES, 'UTF-8'); ?>">
                    <input type="hidden" name="id" value="<?php echo (int) ($student['id'] ?? 0); ?>">
                    <div class="mb-3">
                        <label class="form-label" for="izenaInput"><?php echo htmlspecialchars($lang['name'], ENT_QUOTES, 'UTF-8'); ?></label>
                        <input type="text" class="form-control <?php echo !empty($errors['izena']) ? 'is-invalid' : ''; ?>" id="izenaInput" name="izena" required maxlength="100" pattern="^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{2,100}$" title="<?php echo htmlspecialchars($lang['error_invalid_name'], ENT_QUOTES, 'UTF-8'); ?>" value="<?php echo htmlspecialchars($old['izena'] ?? ($student['izena'] ?? ''), ENT_QUOTES, 'UTF-8'); ?>">
                        <?php if (!empty($errors['izena'])): ?><div class="invalid-feedback d-block"><?php echo htmlspecialchars($errors['izena'], ENT_QUOTES, 'UTF-8'); ?></div><?php endif; ?>
                    </div>
                    <div class="mb-3">
                        <label class="form-label" for="abizenaInput"><?php echo htmlspecialchars($lang['surname'], ENT_QUOTES, 'UTF-8'); ?></label>
                        <input type="text" class="form-control <?php echo !empty($errors['abizena']) ? 'is-invalid' : ''; ?>" id="abizenaInput" name="abizena" required maxlength="100" pattern="^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{2,100}$" title="<?php echo htmlspecialchars($lang['error_invalid_name'], ENT_QUOTES, 'UTF-8'); ?>" value="<?php echo htmlspecialchars($old['abizena'] ?? ($student['abizena'] ?? ''), ENT_QUOTES, 'UTF-8'); ?>">
                        <?php if (!empty($errors['abizena'])): ?><div class="invalid-feedback d-block"><?php echo htmlspecialchars($errors['abizena'], ENT_QUOTES, 'UTF-8'); ?></div><?php endif; ?>
                    </div>
                    <div class="mb-3">
                        <label class="form-label" for="zikloaInput"><?php echo htmlspecialchars($lang['cycle'], ENT_QUOTES, 'UTF-8'); ?></label>
                        <input type="text" class="form-control <?php echo !empty($errors['zikloa']) ? 'is-invalid' : ''; ?>" id="zikloaInput" name="zikloa" required maxlength="100" value="<?php echo htmlspecialchars($old['zikloa'] ?? ($student['zikloa'] ?? ''), ENT_QUOTES, 'UTF-8'); ?>">
                        <?php if (!empty($errors['zikloa'])): ?><div class="invalid-feedback d-block"><?php echo htmlspecialchars($errors['zikloa'], ENT_QUOTES, 'UTF-8'); ?></div><?php endif; ?>
                    </div>
                    <div class="mb-3">
                        <label class="form-label" for="mailaInput"><?php echo htmlspecialchars($lang['level'], ENT_QUOTES, 'UTF-8'); ?></label>
                        <input type="text" class="form-control <?php echo !empty($errors['maila']) ? 'is-invalid' : ''; ?>" id="mailaInput" name="maila" required maxlength="50" value="<?php echo htmlspecialchars($old['maila'] ?? ($student['maila'] ?? ''), ENT_QUOTES, 'UTF-8'); ?>">
                        <?php if (!empty($errors['maila'])): ?><div class="invalid-feedback d-block"><?php echo htmlspecialchars($errors['maila'], ENT_QUOTES, 'UTF-8'); ?></div><?php endif; ?>
                    </div>
                    <div class="mb-3">
                        <label class="form-label" for="argazkiaInput"><?php echo htmlspecialchars($lang['photo'], ENT_QUOTES, 'UTF-8'); ?></label>
                        <input type="file" class="form-control <?php echo !empty($errors['argazkia']) ? 'is-invalid' : ''; ?>" id="argazkiaInput" name="argazkia" accept="image/jpeg,image/png,image/webp">
                        <div class="form-text"><?php echo htmlspecialchars($lang['upload_help'], ENT_QUOTES, 'UTF-8'); ?></div>
                        <?php if (!empty($student['argazkia'])): ?>
                            <div class="mt-2">
                                <span class="fw-semibold"><?php echo htmlspecialchars($lang['current_photo'], ENT_QUOTES, 'UTF-8'); ?>:</span>
                                <?php $currentPhoto = rtrim($baseUrl, '/'); $currentPhoto = ($currentPhoto === '' ? '' : $currentPhoto) . '/' . ltrim($student['argazkia'], '/'); ?>
                                <img class="img-thumbnail ms-2" style="width:85px;height:85px;object-fit:cover;" src="<?php echo htmlspecialchars($currentPhoto, ENT_QUOTES, 'UTF-8'); ?>" alt="current">
                            </div>
                        <?php endif; ?>
                        <?php if (!empty($errors['argazkia'])): ?><div class="invalid-feedback d-block"><?php echo htmlspecialchars($errors['argazkia'], ENT_QUOTES, 'UTF-8'); ?></div><?php endif; ?>
                    </div>
                    <div class="d-flex justify-content-between">
                        <a class="btn btn-outline-secondary" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php"><?php echo htmlspecialchars($lang['back'], ENT_QUOTES, 'UTF-8'); ?></a>
                        <button class="btn btn-primary" type="submit"><?php echo htmlspecialchars($lang['save_changes'], ENT_QUOTES, 'UTF-8'); ?></button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<!-- Bezero aldean fitxategi tamaina kontrolatzen da -->
<script>
(function () {
    const form = document.getElementById('editForm');
    if (!form) return;
    form.addEventListener('submit', function (event) {
        const fileInput = document.getElementById('argazkiaInput');
        if (fileInput && fileInput.files[0] && fileInput.files[0].size > 2 * 1024 * 1024) {
            event.preventDefault();
            alert('<?php echo addslashes($lang['upload_help']); ?>');
        }
    });
})();
</script>
<?php require __DIR__ . '/layout/footer.php'; ?>
