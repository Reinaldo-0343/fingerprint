CREATE DATABASE sistema_fichatge;

CREATE TABLE emprentes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuari VARCHAR(50) NOT NULL,
    emprenta BLOB NOT NULL,
    data_registre TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
