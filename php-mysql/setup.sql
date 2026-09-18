-- Ikasleen datu-basea sortu (PHP + MySQL froga)
-- Exekutatu: sudo mysql < setup.sql

CREATE DATABASE IF NOT EXISTS ikasleak
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'ikaslea'@'localhost' IDENTIFIED BY 'ikaslea123';
GRANT ALL PRIVILEGES ON ikasleak.* TO 'ikaslea'@'localhost';
FLUSH PRIVILEGES;

USE ikasleak;

CREATE TABLE IF NOT EXISTS ikasleak (
  id INT AUTO_INCREMENT PRIMARY KEY,
  izena VARCHAR(100) NOT NULL,
  emaila VARCHAR(150) NOT NULL,
  sortua TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Adibide datuak (bakarrik taula hutsa badago)
INSERT INTO ikasleak (izena, emaila)
SELECT * FROM (
  SELECT 'Ane Lopez' AS izena, 'ane@example.com' AS emaila
) AS tmp
WHERE NOT EXISTS (SELECT 1 FROM ikasleak LIMIT 1);

INSERT INTO ikasleak (izena, emaila)
SELECT 'Mikel Garcia', 'mikel@example.com'
FROM DUAL
WHERE (SELECT COUNT(*) FROM ikasleak) < 2;

INSERT INTO ikasleak (izena, emaila)
SELECT 'Leire Ruiz', 'leire@example.com'
FROM DUAL
WHERE (SELECT COUNT(*) FROM ikasleak) < 3;
