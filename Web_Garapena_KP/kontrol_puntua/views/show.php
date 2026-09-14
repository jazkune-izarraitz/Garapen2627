<?php require __DIR__ . '/layout/header.php'; ?>
<!-- Ikasle bakarraren xehetasunak -->
<div class="row justify-content-center">
    <div class="col-lg-6">
        <div class="card profile-card shadow-lg">
            <div class="card-header bg-white">
                <h5 class="mb-0"><?php echo htmlspecialchars($student['izena'] ?? '', ENT_QUOTES, 'UTF-8'); ?> <?php echo htmlspecialchars($student['abizena'] ?? '', ENT_QUOTES, 'UTF-8'); ?></h5>
            </div>
            <div class="card-body">
                <?php if (!empty($student['argazkia'])): ?>
                    <!-- Argazki biribildua -->
                    <?php $photoUrl = rtrim($baseUrl, '/'); $photoUrl = ($photoUrl === '' ? '' : $photoUrl) . '/' . ltrim($student['argazkia'], '/'); ?>
                    <div class="text-center mb-3">
                        <img class="rounded-circle border" style="width:140px;height:140px;object-fit:cover;" src="<?php echo htmlspecialchars($photoUrl, ENT_QUOTES, 'UTF-8'); ?>" alt="profile">
                    </div>
                <?php endif; ?>
                <dl class="row mb-0">
                    <dt class="col-sm-4"><?php echo htmlspecialchars($lang['cycle'], ENT_QUOTES, 'UTF-8'); ?></dt>
                    <dd class="col-sm-8"><?php echo htmlspecialchars($student['zikloa'] ?? '', ENT_QUOTES, 'UTF-8'); ?></dd>
                    <dt class="col-sm-4"><?php echo htmlspecialchars($lang['level'], ENT_QUOTES, 'UTF-8'); ?></dt>
                    <dd class="col-sm-8"><?php echo htmlspecialchars($student['maila'] ?? '', ENT_QUOTES, 'UTF-8'); ?></dd>
                    <dt class="col-sm-4">ID</dt>
                    <dd class="col-sm-8"><?php echo (int) ($student['id'] ?? 0); ?></dd>
                </dl>
            </div>
            <div class="card-footer d-flex justify-content-between bg-white">
                <a class="btn btn-outline-secondary" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php"><?php echo htmlspecialchars($lang['back'], ENT_QUOTES, 'UTF-8'); ?></a>
                <a class="btn btn-primary" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=edit&id=<?php echo (int) ($student['id'] ?? 0); ?>"><?php echo htmlspecialchars($lang['edit'], ENT_QUOTES, 'UTF-8'); ?></a>
            </div>
        </div>
    </div>
</div>
<?php require __DIR__ . '/layout/footer.php'; ?>
