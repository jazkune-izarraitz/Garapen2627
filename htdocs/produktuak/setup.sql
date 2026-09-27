-- Denda datu-basea eta produktuak taula
-- Exekutatu Docker MySQL-n, adibidez:
--   docker exec -i mysql-30-0-8 mysql -uroot -proot < setup.sql
-- edo ostalarian:
--   mysql -h127.0.0.1 -P3306 -uroot -proot < setup.sql

CREATE DATABASE IF NOT EXISTS denda
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'denda'@'%' IDENTIFIED BY 'denda123';
GRANT ALL PRIVILEGES ON denda.* TO 'denda'@'%';
FLUSH PRIVILEGES;

USE denda;

CREATE TABLE IF NOT EXISTS produktuak (
  id INT AUTO_INCREMENT PRIMARY KEY,
  izena VARCHAR(100) NOT NULL,
  deskribapena TEXT,
  prezioa DECIMAL(6,2) NOT NULL,
  irudia VARCHAR(255)
);

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT * FROM (
  SELECT
    'Te klasekoa' AS izena,
    'Te beltza organikoa, 100g. Goizeko energia lasai baterako.' AS deskribapena,
    4.50 AS prezioa,
    'te.png' AS irudia
) AS t
WHERE NOT EXISTS (SELECT 1 FROM produktuak LIMIT 1);

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT
  'Kafe aleak',
  'Arabica ale erreak, 250g. Usain sakona eta zapore orekatua.',
  8.90,
  'kafea.png'
FROM DUAL
WHERE (SELECT COUNT(*) FROM produktuak) < 2;

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT
  'Txokolate beltza',
  '70% kakaoa, 100g. Goxotasun orekatua azukre gutxirekin.',
  3.20,
  'txokolatea.png'
FROM DUAL
WHERE (SELECT COUNT(*) FROM produktuak) < 3;
