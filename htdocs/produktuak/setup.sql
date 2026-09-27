-- Denda DB + produktuak taula
-- docker exec -i mysql-30-0-8 mysql -uroot -p2paag3 < setup.sql

CREATE DATABASE IF NOT EXISTS denda CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE denda;

CREATE TABLE IF NOT EXISTS produktuak (
  id INT AUTO_INCREMENT PRIMARY KEY,
  izena VARCHAR(100) NOT NULL,
  deskribapena TEXT,
  prezioa DECIMAL(6,2) NOT NULL,
  irudia VARCHAR(255)
);

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT 'Te klasekoa', 'Te beltza organikoa, 100g.', 4.50, 'te.png'
WHERE NOT EXISTS (SELECT 1 FROM produktuak LIMIT 1);

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT 'Kafe aleak', 'Arabica ale erreak, 250g.', 8.90, 'kafea.png'
WHERE (SELECT COUNT(*) FROM produktuak) < 2;

INSERT INTO produktuak (izena, deskribapena, prezioa, irudia)
SELECT 'Txokolate beltza', '70% kakaoa, 100g.', 3.20, 'txokolatea.png'
WHERE (SELECT COUNT(*) FROM produktuak) < 3;
