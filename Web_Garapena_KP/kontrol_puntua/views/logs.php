<?php require __DIR__ . '/layout/header.php'; ?>
<!-- Aplikazioaren log bistaratzailea -->
<div class="row justify-content-center">
    <div class="col-xl-10">
        <div class="card logs-card shadow-lg">
            <div class="card-header bg-white d-flex flex-wrap justify-content-between align-items-center gap-2">
                <div>
                    <h5 class="mb-0 text-uppercase text-muted small">LOGS</h5>
                    <h3 class="mb-0 fw-semibold text-dark"><?php echo htmlspecialchars($lang['logs_title'], ENT_QUOTES, 'UTF-8'); ?></h3>
                    <span class="text-muted small"><?php echo htmlspecialchars($logFileRelative ?? 'logs/app.log', ENT_QUOTES, 'UTF-8'); ?></span>
                </div>
                <div class="d-flex gap-2">
                    <a class="btn btn-outline-secondary" href="<?php echo htmlspecialchars($baseUrl, ENT_QUOTES, 'UTF-8'); ?>/index.php">
                        <?php echo htmlspecialchars($lang['back'], ENT_QUOTES, 'UTF-8'); ?>
                    </a>
                </div>
            </div>
            <div class="card-body">
                <?php if (empty($logEntries)): ?>
                    <div class="alert alert-info mb-0">
                        <?php echo htmlspecialchars($lang['logs_empty'], ENT_QUOTES, 'UTF-8'); ?>
                    </div>
                <?php else: ?>
                    <!-- Log taula eskalagarria -->
                    <div class="table-responsive log-table-wrapper">
                        <table class="table table-modern log-table align-middle">
                            <thead>
                                <tr>
                                    <th>Timestamp</th>
                                    <th>User</th>
                                    <th>Action</th>
                                    <th>ID</th>
                                    <th><?php echo htmlspecialchars($lang['log_details'], ENT_QUOTES, 'UTF-8'); ?></th>
                                </tr>
                            </thead>
                            <tbody>
                            <?php foreach ($logEntries as $entry): ?>
                                <tr>
                                    <td><?php echo htmlspecialchars($entry['timestamp'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td><?php echo htmlspecialchars($entry['user'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td><span class="badge rounded-pill text-bg-primary text-uppercase"><?php echo htmlspecialchars($entry['action'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></span></td>
                                    <td><?php echo htmlspecialchars($entry['id'] ?? '—', ENT_QUOTES, 'UTF-8'); ?></td>
                                    <td>
                                        <?php if (!empty($entry['data']) && is_array($entry['data'])): ?>
                                            <pre class="log-json"><?php echo htmlspecialchars(json_encode($entry['data'], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), ENT_QUOTES, 'UTF-8'); ?></pre>
                                        <?php elseif (!empty($entry['data'])): ?>
                                            <pre class="log-json"><?php echo htmlspecialchars((string) $entry['data'], ENT_QUOTES, 'UTF-8'); ?></pre>
                                        <?php elseif (!empty($entry['extra'])): ?>
                                            <span class="text-muted small"><?php echo htmlspecialchars($entry['extra'], ENT_QUOTES, 'UTF-8'); ?></span>
                                        <?php else: ?>
                                            <span class="text-muted">—</span>
                                        <?php endif; ?>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</div>
<?php require __DIR__ . '/layout/footer.php'; ?>
