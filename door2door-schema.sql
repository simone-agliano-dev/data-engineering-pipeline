CREATE DATABASE door2door;
USE door2door;

CREATE TABLE events (
    id BIGINT UNSIGNED NOT NULL UNIQUE,
    file VARCHAR(100) NOT NULL,
    event varchar(50) NOT NULL,
    on_event varchar(50) NOT NULL,
    at_event DATETIME NOT NULL,
    organization_id varchar(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE vehicles (
    id_event BIGINT UNSIGNED  NOT NULL UNIQUE,
    id_vehicle VARCHAR(50) NOT NULL,
    lat DECIMAL(10, 8),
    lng DECIMAL(10, 8),
    at_vehicle DATETIME,
    FOREIGN KEY(id_event) REFERENCES events(id) ON DELETE CASCADE
);


CREATE TABLE operating_period (
    id_event BIGINT UNSIGNED  NOT NULL UNIQUE,
    id_operating VARCHAR(50) NOT NULL,
    start DATETIME NOT NULL,
    finish DATETIME NOT NULL,
    FOREIGN KEY(id_event) REFERENCES events(id) ON DELETE CASCADE
);