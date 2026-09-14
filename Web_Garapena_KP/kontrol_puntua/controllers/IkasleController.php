<?php
declare(strict_types=1);

require_once __DIR__ . '/../models/Ikasle.php';

/**
 * Ikasle Controller nagusia: negozio logika eta ikuspegiak kudeatzen ditu.
 * Euskal komentarioek argi azaltzen dute eskalagarritasun eta segurtasun neurriak.
 */
class IkasleController
{
    /** @var Ikasle Datu-eredua injektatuta */
    private Ikasle $model;
    /** @var array Itzulpen kate guztiak */
    private array $translations;
    /** @var array Uneko hizkuntzaren kateak */
    private array $activeLang;
    /** @var string Saioan gordetzen den erabiltzaile sinonimoa */
    private string $currentUser;
    /** @var int Orrialdeko erakusteko ikasle kopurua */
    private int $perPage = 10;

    /**
     * @param PDO $pdo Erabiliko den PDO konexioa
     * @param array $translations UIan erabiliko diren hizkuntza baliabideak
     */
    public function __construct(PDO $pdo, array $translations)
    {
        $this->model = new Ikasle($pdo);
        $this->translations = $translations;
        $this->currentUser = $_SESSION['user'] ?? 'admin';
        $_SESSION['user'] = $this->currentUser;

        $this->bootstrapLanguage();
        $this->ensureCsrfToken();
        $this->logLoginOnce();
    }

    /**
     * Hasierako zerrenda bistaratzen du bilaketa, ordenazio eta orrikatzearekin.
     */
    public function index(): void
    {
        $search = trim((string) ($_GET['search'] ?? ''));
        $order = (string) ($_GET['order'] ?? 'izena');
        $dir = (string) ($_GET['dir'] ?? 'ASC');
        $page = max(1, (int) ($_GET['page'] ?? 1));

        $searchTerm = $search !== '' ? $search : null;
        $totalStudents = $this->model->countAll($searchTerm);
        $totalPages = max(1, (int) ceil($totalStudents / $this->perPage));
        if ($page > $totalPages) {
            $page = $totalPages;
        }
        $offset = ($page - 1) * $this->perPage;

        $students = $this->model->all($searchTerm, $order, $dir, $this->perPage, $offset);

        if ($search !== '') {
            $this->logAction('search', ['term' => $search]);
        }

        $this->render('index', [
            'students' => $students,
            'search' => $search,
            'order' => $order,
            'dir' => strtoupper($dir) === 'DESC' ? 'DESC' : 'ASC',
            'pagination' => [
                'page' => $page,
                'totalPages' => $totalPages,
                'total' => $totalStudents,
                'perPage' => $this->perPage,
            ],
            'query' => [
                'search' => $search,
                'order' => $order,
                'dir' => strtoupper($dir) === 'DESC' ? 'DESC' : 'ASC',
            ],
        ]);
    }

    /**
     * Alta formularioa erakusten du errore edo datu zaharrekin.
     */
    public function create(array $errors = [], array $old = []): void
    {
        $this->render('create', compact('errors', 'old'));
    }

    /**
     * POST bidez jasotako datuak balidatu eta gorde.
     */
    public function store(): void
    {
        $this->guardPost();
        if (!$this->isValidCsrf($_POST['csrf_token'] ?? '')) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $data = $this->filterInput();
        $errors = $this->validateInput($data);

        $photo = null;
        try {
            $photo = $this->handleUpload($_FILES['argazkia'] ?? null);
        } catch (RuntimeException $e) {
            $errors['argazkia'] = $e->getMessage();
        }

        if ((!isset($_FILES['argazkia']) || ($_FILES['argazkia']['error'] ?? UPLOAD_ERR_NO_FILE) === UPLOAD_ERR_NO_FILE) && empty($errors['argazkia'])) {
            $errors['argazkia'] = $this->activeLang['upload_help'];
        }

        if (!empty($errors)) {
            $this->create($errors, $data);
            return;
        }

        $data['argazkia'] = $photo;

        try {
            $this->model->create($data);
            $this->flash('success', $this->activeLang['success_add']);
            $this->logAction('insert', ['izena' => $data['izena'], 'maila' => $data['maila']]);
            $this->redirect();
        } catch (Throwable $e) {
            error_log($e->getMessage());
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect('action=create');
        }
    }

    /**
     * Editatzeko formularioa erakusten du IDaren arabera.
     */
    public function edit(): void
    {
        $id = (int) ($_GET['id'] ?? 0);
        $student = $this->model->find($id);

        if (!$student) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $this->render('edit', ['student' => $student, 'errors' => [], 'old' => $student]);
    }

    /**
     * Editatutako datuak balidatu eta eguneratu.
     */
    public function update(): void
    {
        $this->guardPost();
        if (!$this->isValidCsrf($_POST['csrf_token'] ?? '')) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $id = (int) ($_POST['id'] ?? 0);
        $existing = $this->model->find($id);
        if (!$existing) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $data = $this->filterInput();
        $errors = $this->validateInput($data);

        try {
            $photo = $this->handleUpload($_FILES['argazkia'] ?? null, $existing['argazkia']);
        } catch (RuntimeException $e) {
            $errors['argazkia'] = $e->getMessage();
            $photo = $existing['argazkia'];
        }

        if (!empty($errors)) {
            $this->render('edit', ['student' => $existing, 'errors' => $errors, 'old' => array_merge($existing, $data)]);
            return;
        }

        $data['argazkia'] = $photo ?? $existing['argazkia'];

        try {
            $this->model->update($id, $data);
            $this->flash('success', $this->activeLang['success_update']);
            $this->logAction('update', ['id' => $id]);
            $this->redirect();
        } catch (Throwable $e) {
            error_log($e->getMessage());
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect('action=edit&id=' . $id);
        }
    }

    /**
     * Ikaslea eta bere argazkia ezabatzen ditu.
     */
    public function delete(): void
    {
        $this->guardPost();
        if (!$this->isValidCsrf($_POST['csrf_token'] ?? '')) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $id = (int) ($_POST['id'] ?? 0);
        $student = $this->model->find($id);

        if (!$student) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        try {
            $this->model->delete($id);
            if (!empty($student['argazkia'])) {
                $this->deleteFile($student['argazkia']);
            }
            $this->flash('success', $this->activeLang['success_delete']);
            $this->logAction('delete', ['id' => $id]);
        } catch (Throwable $e) {
            error_log($e->getMessage());
            $this->flash('danger', $this->activeLang['error_generic']);
        }

        $this->redirect();
    }

    /**
     * Ikaslearen xehetasun ikuspegia erakusten du.
     */
    public function show(): void
    {
        $id = (int) ($_GET['id'] ?? 0);
        $student = $this->model->find($id);

        if (!$student) {
            $this->flash('danger', $this->activeLang['error_generic']);
            $this->redirect();
        }

        $this->render('show', ['student' => $student]);
    }

    /**
     * Aplikazioaren log fitxategia modu bisualean bistaratzen du.
     */
    public function logs(): void
    {
        $logFile = dirname(__DIR__) . '/logs/app.log';
        $entries = [];

        if (is_readable($logFile)) {
            $lines = file($logFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
            foreach (array_reverse($lines) as $line) {
                $entries[] = $this->formatLogLine($line);
            }
        }

        $this->render('logs', [
            'logEntries' => $entries,
            'logFile' => $logFile,
            'logFileRelative' => 'logs/app.log',
        ]);
    }

    /**
     * Hizkuntza kargatzen du GET edo saioaren arabera.
     */
    private function bootstrapLanguage(): void
    {
        if (isset($_GET['lang']) && array_key_exists($_GET['lang'], $this->translations)) {
            $_SESSION['lang'] = $_GET['lang'];
        }

        $selected = $_SESSION['lang'] ?? 'eu';
        if (!array_key_exists($selected, $this->translations)) {
            $selected = 'eu';
            $_SESSION['lang'] = $selected;
        }

        $this->activeLang = $this->translations[$selected];
    }

    /**
     * CSRF tokena sortzen du saioan baldin ez badago.
     */
    private function ensureCsrfToken(): void
    {
        if (empty($_SESSION['csrf_token'])) {
            $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
        }
    }

    /**
     * Saio bakoitzean behin soilik login ekintza erregistratzen du.
     */
    private function logLoginOnce(): void
    {
        if (empty($_SESSION['logged_once'])) {
            $_SESSION['logged_once'] = true;
            $this->logAction('login');
        }
    }

    /**
     * Egindako ekintza orok log fitxategian erregistratzen du JSON datuekin.
     */
    private function logAction(string $action, array $context = []): void
    {
        $logFile = dirname(__DIR__) . '/logs/app.log';
        $base = sprintf('[%s] USER:%s ACTION:%s', date('Y-m-d H:i:s'), $this->currentUser, $action);

        if (isset($context['id'])) {
            $base .= ' ID:' . $context['id'];
            unset($context['id']);
        }

        if (!empty($context)) {
            $base .= ' DATA:' . json_encode($context, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        }

        file_put_contents($logFile, $base . PHP_EOL, FILE_APPEND | LOCK_EX);
    }

    /**
     * Partekatutako datuak prestatu eta ikuspegia kargatzen du.
     */
    private function render(string $view, array $data = []): void
    {
        $lang = $this->activeLang;
        $currentLang = $_SESSION['lang'] ?? 'eu';
        $availableLanguages = array_keys($this->translations);
        $csrfToken = $_SESSION['csrf_token'];
        $flash = $this->consumeFlash();
        $baseUrl = defined('BASE_URL') ? BASE_URL : '';

        extract($data);
        require __DIR__ . '/../views/' . $view . '.php';
    }

    /**
     * Erabiltzailearen sarrera moztu, garbitu eta gehienezko luzera mugatzen du.
     */
    private function filterInput(): array
    {
        $fields = [
            'izena' => 100,
            'abizena' => 100,
            'zikloa' => 100,
            'maila' => 50,
        ];
        $clean = [];
        foreach ($fields as $field => $maxLength) {
            $value = trim((string) ($_POST[$field] ?? ''));
            $value = strip_tags($value);
            $clean[$field] = mb_substr($value, 0, $maxLength, 'UTF-8');
        }

        return $clean;
    }

    /**
     * Beharrezko eremuak eta izenaren patroiak balidatzen ditu.
     */
    private function validateInput(array $data): array
    {
        $errors = [];
        foreach ($data as $key => $value) {
            if ($value === '') {
                $errors[$key] = $this->activeLang['error_required'];
                continue;
            }

            if (in_array($key, ['izena', 'abizena'], true) && !$this->isValidName($value)) {
                $errors[$key] = $this->activeLang['error_invalid_name'];
            }
        }
        return $errors;
    }

    /**
     * Irudi igoerak balidatu eta gordetzen ditu, aurreko fitxategia garbituz.
     */
    private function handleUpload(?array $file, ?string $existing = null): ?string
    {
        if (!$file || $file['error'] === UPLOAD_ERR_NO_FILE) {
            return $existing;
        }

        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new RuntimeException($this->activeLang['error_generic']);
        }

        if ($file['size'] > 2 * 1024 * 1024) {
            throw new RuntimeException($this->activeLang['upload_help']);
        }

        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime = $finfo->file($file['tmp_name']);
        $allowed = [
            'image/jpeg' => 'jpg',
            'image/png' => 'png',
            'image/webp' => 'webp',
        ];

        if (!array_key_exists($mime, $allowed)) {
            throw new RuntimeException($this->activeLang['upload_help']);
        }

        $extension = $allowed[$mime];
        $safeName = preg_replace('/[^A-Za-z0-9_\-]/', '_', pathinfo($file['name'], PATHINFO_FILENAME));
        $newName = time() . '_' . $safeName . '.' . $extension;
        $destinationDir = dirname(__DIR__) . '/public/uploads/';
        $destinationPath = $destinationDir . $newName;

        if (!move_uploaded_file($file['tmp_name'], $destinationPath)) {
            throw new RuntimeException($this->activeLang['error_generic']);
        }

        if ($existing && $existing !== '') {
            $this->deleteFile($existing);
        }

        return 'uploads/' . $newName;
    }

    /**
     * Fitxategi erlatiboa sistematik kentzen du bada.
     */
    private function deleteFile(string $relativePath): void
    {
        $cleanPath = ltrim($relativePath, '/\\');
        $fullPath = dirname(__DIR__) . '/public/' . $cleanPath;
        if (is_file($fullPath)) {
            @unlink($fullPath);
        }
    }

    /**
     * Izenek soilik letrak eta baimendutako karaktereak dutela bermatzen du.
     */
    private function isValidName(string $value): bool
    {
        $value = trim($value);
        if ($value === '') {
            return false;
        }

        return (bool) preg_match('/^[A-Za-zÀ-ÖØ-öø-ÿ\\s\'-]{2,100}$/u', $value);
    }

    /**
     * Log lerro bakoitza analizatu eta egitura eroso batera bihurtzen du.
     */
    private function formatLogLine(string $line): array
    {
        $entry = [
            'timestamp' => null,
            'user' => null,
            'action' => null,
            'id' => null,
            'data' => null,
            'extra' => '',
            'raw' => $line,
        ];

        if (preg_match('/^\[(.*?)\]\s+USER:([^ ]+)\s+ACTION:([^ ]+)\s*(.*)$/u', $line, $matches)) {
            $entry['timestamp'] = $matches[1];
            $entry['user'] = $matches[2];
            $entry['action'] = $matches[3];
            $tail = trim($matches[4]);

            if ($tail !== '') {
                if (preg_match('/ID:(\d+)/', $tail, $idMatch)) {
                    $entry['id'] = $idMatch[1];
                    $tail = trim(str_replace($idMatch[0], '', $tail));
                }

                if (preg_match('/DATA:(\{.*\})/u', $tail, $dataMatch)) {
                    $decoded = json_decode($dataMatch[1], true);
                    $entry['data'] = $decoded ?? $dataMatch[1];
                    $tail = trim(str_replace($dataMatch[0], '', $tail));
                }

                $entry['extra'] = $tail;
            }
        }

        return $entry;
    }

    /**
     * POST ez den eskaera batek index-era birbideratuko du.
     */
    private function guardPost(): void
    {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            $this->redirect();
        }
    }

    /**
     * CSRF tokenaren egiaztapena egiten du.
     */
    private function isValidCsrf(string $token): bool
    {
        return isset($_SESSION['csrf_token']) && hash_equals($_SESSION['csrf_token'], $token);
    }

    /**
     * Flash mezua saioan gordetzen du erabiltzaileari feedbacka emateko.
     */
    private function flash(string $type, string $message): void
    {
        $_SESSION['flash'] = ['type' => $type, 'message' => $message];
    }

    /**
     * Flash mezua behin bakarrik erakusten da; metodo honek kontsumitzen du.
     */
    private function consumeFlash(): ?array
    {
        if (!empty($_SESSION['flash'])) {
            $flash = $_SESSION['flash'];
            unset($_SESSION['flash']);
            return $flash;
        }
        return null;
    }

    /**
     * Erabiltzailea definitutako URLera birbideratzen du kontsulta parametroekin.
     */
    private function redirect(string $query = ''): void
    {
        $target = (defined('BASE_URL') ? BASE_URL : '') . '/index.php';
        if ($query !== '') {
            $target .= '?' . $query;
        }
        header('Location: ' . $target);
        exit;
    }
}
