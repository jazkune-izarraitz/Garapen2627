<?php require __DIR__ . '/layout/header.php'; ?>
<!-- Hasierako zerrendaren aldagai kalkulatuak -->
<?php
    $queryBase = $query ?? [
        'search' => $search ?? '',
        'order' => $order ?? 'izena',
        'dir' => $dir ?? 'ASC',
    ];
    $currentPage = $pagination['page'] ?? 1;
    $totalPages = $pagination['totalPages'] ?? 1;
    $totalRecords = $pagination['total'] ?? count($students ?? []);
    $perPageCount = $pagination['perPage'] ?? 10;
    $startRecord = $totalRecords > 0 ? (($currentPage - 1) * $perPageCount) + 1 : 0;
    $endRecord = $totalRecords > 0 ? min($startRecord + $perPageCount - 1, $totalRecords) : 0;
    $buildPageUrl = function (int $page) use ($queryBase, $baseUrl) {
        $params = array_filter($queryBase, static fn ($value) => $value !== '' && $value !== null);
        $params['page'] = $page;
        $queryString = http_build_query($params);
        return $baseUrl . '/index.php' . ($queryString ? '?' . $queryString : '');
    };
?>
<!-- Bilaketa eta ordenazio panel bisuala -->
<div class="card filter-card shadow-lg mb-4">
    <div class="card-body">
        <form class="row gy-2 gx-3 align-items-end" method="get" action="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php">
            <input type="hidden" name="page" value="1">
            <div class="col-md-4">
                <label class="form-label fw-semibold" for="searchInput"><?php echo htmlspecialchars($lang['search'], ENT_QUOTES, 'UTF-8'); ?></label>
                <input type="text" class="form-control" id="searchInput" name="search" placeholder="<?php echo htmlspecialchars($lang['search_placeholder'], ENT_QUOTES, 'UTF-8'); ?>" value="<?php echo htmlspecialchars($search ?? '', ENT_QUOTES, 'UTF-8'); ?>">
            </div>
            <div class="col-md-4">
                <label class="form-label fw-semibold" for="orderSelect"><?php echo htmlspecialchars($lang['order_by'], ENT_QUOTES, 'UTF-8'); ?></label>
                <select name="order" id="orderSelect" class="form-select">
                    <option value="izena" <?php echo ($order ?? '') === 'izena' ? 'selected' : ''; ?>><?php echo htmlspecialchars($lang['sort_izena'], ENT_QUOTES, 'UTF-8'); ?></option>
                    <option value="zikloa" <?php echo ($order ?? '') === 'zikloa' ? 'selected' : ''; ?>><?php echo htmlspecialchars($lang['sort_zikloa'], ENT_QUOTES, 'UTF-8'); ?></option>
                    <option value="maila" <?php echo ($order ?? '') === 'maila' ? 'selected' : ''; ?>><?php echo htmlspecialchars($lang['sort_maila'], ENT_QUOTES, 'UTF-8'); ?></option>
                </select>
            </div>
            <div class="col-md-2">
                <label class="form-label fw-semibold" for="dirSelect">ASC/DESC</label>
                <select name="dir" id="dirSelect" class="form-select">
                    <option value="ASC" <?php echo ($dir ?? '') === 'ASC' ? 'selected' : ''; ?>>ASC</option>
                    <option value="DESC" <?php echo ($dir ?? '') === 'DESC' ? 'selected' : ''; ?>>DESC</option>
                </select>
            </div>
            <div class="col-md-2 d-grid">
                <button class="btn btn-primary" type="submit"><?php echo htmlspecialchars($lang['search'], ENT_QUOTES, 'UTF-8'); ?></button>
            </div>
        </form>
    </div>
</div>

<?php if (empty($students)): ?>
    <!-- Ez dagoen kasuan informazio mezua -->
    <div class="alert alert-info">
        <?php echo htmlspecialchars($lang['no_students'], ENT_QUOTES, 'UTF-8'); ?>
    </div>
<?php else: ?>
    <!-- Ikasleen taula nagusia -->
    <div class="table-responsive shadow-sm">
        <table class="table table-modern align-middle">
            <thead class="table-light">
                <tr>
                    <th><?php echo htmlspecialchars($lang['name'], ENT_QUOTES, 'UTF-8'); ?></th>
                    <th><?php echo htmlspecialchars($lang['surname'], ENT_QUOTES, 'UTF-8'); ?></th>
                    <th><?php echo htmlspecialchars($lang['cycle'], ENT_QUOTES, 'UTF-8'); ?></th>
                    <th><?php echo htmlspecialchars($lang['level'], ENT_QUOTES, 'UTF-8'); ?></th>
                    <th><?php echo htmlspecialchars($lang['photo'], ENT_QUOTES, 'UTF-8'); ?></th>
                    <th><?php echo htmlspecialchars($lang['actions'], ENT_QUOTES, 'UTF-8'); ?></th>
                </tr>
            </thead>
            <tbody>
            <?php foreach ($students as $student): ?>
                <tr>
                    <td><?php echo htmlspecialchars($student['izena'], ENT_QUOTES, 'UTF-8'); ?></td>
                    <td><?php echo htmlspecialchars($student['abizena'], ENT_QUOTES, 'UTF-8'); ?></td>
                    <td><?php echo htmlspecialchars($student['zikloa'], ENT_QUOTES, 'UTF-8'); ?></td>
                    <td><?php echo htmlspecialchars($student['maila'], ENT_QUOTES, 'UTF-8'); ?></td>
                    <td>
                        <?php if (!empty($student['argazkia'])): ?>
                            <?php $thumbPath = rtrim($baseUrl, '/'); $thumbPath = ($thumbPath === '' ? '' : $thumbPath) . '/' . ltrim($student['argazkia'], '/'); ?>
                            <img src="<?php echo htmlspecialchars($thumbPath, ENT_QUOTES, 'UTF-8'); ?>" alt="thumb" class="img-thumbnail" style="width:60px;height:60px;object-fit:cover;">
                        <?php else: ?>
                            <span class="text-muted">—</span>
                        <?php endif; ?>
                    </td>
                    <td class="actions-cell">
                        <div class="actions-wrapper d-inline-flex flex-wrap align-items-center gap-2">
                            <a class="btn btn-sm btn-details" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=show&id=<?php echo (int) $student['id']; ?>">
                                <?php echo htmlspecialchars($lang['details'], ENT_QUOTES, 'UTF-8'); ?>
                            </a>
                            <a class="btn btn-sm btn-outline-primary" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=edit&id=<?php echo (int) $student['id']; ?>">
                                <?php echo htmlspecialchars($lang['edit'], ENT_QUOTES, 'UTF-8'); ?>
                            </a>
                            <form method="post" class="d-inline" action="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php?action=delete" onsubmit="return confirm('<?php echo addslashes($lang['confirm_delete']); ?>');">
                                <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($csrfToken, ENT_QUOTES, 'UTF-8'); ?>">
                                <input type="hidden" name="id" value="<?php echo (int) $student['id']; ?>">
                                <button type="submit" class="btn btn-sm btn-danger">
                                    <?php echo htmlspecialchars($lang['delete'], ENT_QUOTES, 'UTF-8'); ?>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php if ($totalRecords > 0): ?>
        <!-- Orrikatze barra -->
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-2 mt-3">
            <span class="text-muted small">
                <?php echo htmlspecialchars($lang['pagination_showing'], ENT_QUOTES, 'UTF-8'); ?>
                <?php echo htmlspecialchars($startRecord, ENT_QUOTES, 'UTF-8'); ?>-<?php echo htmlspecialchars($endRecord, ENT_QUOTES, 'UTF-8'); ?>
                / <?php echo htmlspecialchars($totalRecords, ENT_QUOTES, 'UTF-8'); ?>
            </span>
            <?php if ($totalPages > 1): ?>
                <nav>
                    <ul class="pagination pagination-sm mb-0">
                        <li class="page-item <?php echo $currentPage <= 1 ? 'disabled' : ''; ?>">
                            <?php if ($currentPage <= 1): ?>
                                <span class="page-link"><?php echo htmlspecialchars($lang['pagination_prev'], ENT_QUOTES, 'UTF-8'); ?></span>
                            <?php else: ?>
                                <a class="page-link" href="<?php echo htmlspecialchars($buildPageUrl($currentPage - 1), ENT_QUOTES, 'UTF-8'); ?>">
                                    <?php echo htmlspecialchars($lang['pagination_prev'], ENT_QUOTES, 'UTF-8'); ?>
                                </a>
                            <?php endif; ?>
                        </li>
                        <?php for ($pageNumber = 1; $pageNumber <= $totalPages; $pageNumber++): ?>
                            <li class="page-item <?php echo $pageNumber === $currentPage ? 'active' : ''; ?>">
                                <?php if ($pageNumber === $currentPage): ?>
                                    <span class="page-link"><?php echo $pageNumber; ?></span>
                                <?php else: ?>
                                    <a class="page-link" href="<?php echo htmlspecialchars($buildPageUrl($pageNumber), ENT_QUOTES, 'UTF-8'); ?>"><?php echo $pageNumber; ?></a>
                                <?php endif; ?>
                            </li>
                        <?php endfor; ?>
                        <li class="page-item <?php echo $currentPage >= $totalPages ? 'disabled' : ''; ?>">
                            <?php if ($currentPage >= $totalPages): ?>
                                <span class="page-link"><?php echo htmlspecialchars($lang['pagination_next'], ENT_QUOTES, 'UTF-8'); ?></span>
                            <?php else: ?>
                                <a class="page-link" href="<?php echo htmlspecialchars($buildPageUrl($currentPage + 1), ENT_QUOTES, 'UTF-8'); ?>">
                                    <?php echo htmlspecialchars($lang['pagination_next'], ENT_QUOTES, 'UTF-8'); ?>
                                </a>
                            <?php endif; ?>
                        </li>
                    </ul>
                </nav>
            <?php endif; ?>
        </div>
    <?php endif; ?>
<?php endif; ?>
<?php require __DIR__ . '/layout/footer.php'; ?>
