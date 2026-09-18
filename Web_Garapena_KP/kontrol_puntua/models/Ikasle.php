<?php
declare(strict_types=1);

/**
 * Ikasle datoen eredu geruza.
 * Metodo bakoitzak komentario zehatzak ditu eskalagarritasuna eta mantengarritasuna bermatzeko.
 */
class Ikasle
{
    /**
     * @var PDO Datu-basearen konexioa, injekzio bidez jasotzen dena
     */
    private PDO $db;

    /**
     * @param PDO $db Injektatutako konexioa, probagarritasuna eta eskalagarritasuna errazteko
     */
    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    /**
     * Ikasle guztiak bilatzen ditu iragazki, ordenazio eta orrikatzearekin.
     *
     * @param string|null $search Bilaketa kate globala
     * @param string $orderColumn Ordenatzeko zutabe segurua
     * @param string $orderDir Ordenaren norabidea
     * @param int $limit Orrialde bakoitzeko erregistro kopurua
     * @param int $offset Orrialdearen desplazamendua
     */
    public function all(?string $search, string $orderColumn, string $orderDir, int $limit = 10, int $offset = 0): array
    {
        $allowedColumns = ['izena', 'zikloa', 'maila'];
        $allowedDir = ['ASC', 'DESC'];

        $orderColumn = in_array($orderColumn, $allowedColumns, true) ? $orderColumn : 'izena';
        $orderDir = in_array(strtoupper($orderDir), $allowedDir, true) ? strtoupper($orderDir) : 'ASC';

        $sql = 'SELECT * FROM ikasleak';
        $params = [];

        if (!empty($search)) {
            $sql .= ' WHERE izena LIKE :search_izena OR abizena LIKE :search_abizena';
            $params['search_izena'] = '%' . $search . '%';
            $params['search_abizena'] = '%' . $search . '%';
        }

        $sql .= " ORDER BY {$orderColumn} {$orderDir} LIMIT :limit OFFSET :offset";

        $stmt = $this->db->prepare($sql);
        foreach ($params as $key => $value) {
            $stmt->bindValue(':' . $key, $value, PDO::PARAM_STR);
        }
        $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
        $stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
        $stmt->execute();

        return $stmt->fetchAll();
    }

    /**
     * Bilaketaren emaitza kopurua kalkulatzen du orrikatzea zehaztasunez egiteko.
     */
    public function countAll(?string $search): int
    {
        $sql = 'SELECT COUNT(*) as total FROM ikasleak';
        $params = [];

        if (!empty($search)) {
            $sql .= ' WHERE izena LIKE :search_izena OR abizena LIKE :search_abizena';
            $params['search_izena'] = '%' . $search . '%';
            $params['search_abizena'] = '%' . $search . '%';
        }

        $stmt = $this->db->prepare($sql);
        foreach ($params as $key => $value) {
            $stmt->bindValue(':' . $key, $value, PDO::PARAM_STR);
        }
        $stmt->execute();
        $row = $stmt->fetch();

        return (int) ($row['total'] ?? 0);
    }

    /**
     * ID zehatz baten arabera ikasle bakarra eskuratzen du.
     */
    public function find(int $id): ?array
    {
        $stmt = $this->db->prepare('SELECT * FROM ikasleak WHERE id = :id');
        $stmt->bindValue(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        $result = $stmt->fetch();

        return $result === false ? null : $result;
    }

    /**
     * Ikasle berria sortzen du eta bere IDa bueltatzen.
     */
    public function create(array $data): int
    {
        $stmt = $this->db->prepare('INSERT INTO ikasleak (izena, abizena, zikloa, maila, argazkia) VALUES (:izena, :abizena, :zikloa, :maila, :argazkia)');
        $stmt->execute([
            ':izena' => $data['izena'],
            ':abizena' => $data['abizena'],
            ':zikloa' => $data['zikloa'],
            ':maila' => $data['maila'],
            ':argazkia' => $data['argazkia'],
        ]);

        return (int) $this->db->lastInsertId();
    }

    /**
     * Dagoen ikaslea eguneratzen du datu berriekin.
     */
    public function update(int $id, array $data): bool
    {
        $stmt = $this->db->prepare('UPDATE ikasleak SET izena = :izena, abizena = :abizena, zikloa = :zikloa, maila = :maila, argazkia = :argazkia WHERE id = :id');
        return $stmt->execute([
            ':izena' => $data['izena'],
            ':abizena' => $data['abizena'],
            ':zikloa' => $data['zikloa'],
            ':maila' => $data['maila'],
            ':argazkia' => $data['argazkia'],
            ':id' => $id,
        ]);
    }

    /**
     * Ikaslea datu-basetik ezabatzen du.
     */
    public function delete(int $id): bool
    {
        $stmt = $this->db->prepare('DELETE FROM ikasleak WHERE id = :id');
        return $stmt->execute([':id' => $id]);
    }
}
