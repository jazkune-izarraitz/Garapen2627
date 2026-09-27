-- Denda DB + produktuak taula
-- PowerShell:
--   Get-Content setup.sql | docker exec -i mysql-8-0-30 mysql -uroot -p2paag3
-- CMD / bash:
--   docker exec -i mysql-8-0-30 mysql -uroot -p2paag3 < setup.sql

CREATE DATABASE IF NOT EXISTS denda CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE denda;

CREATE TABLE IF NOT EXISTS produktuak (
  id INT AUTO_INCREMENT PRIMARY KEY,
  izena VARCHAR(100) NOT NULL,
  deskribapena TEXT,
  prezioa DECIMAL(6,2) NOT NULL,
  irudia VARCHAR(255)
);
