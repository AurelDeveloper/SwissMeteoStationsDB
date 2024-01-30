-- smn_database_schema.sql

CREATE TABLE IF NOT EXISTS Stations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    rre150z0 TEXT
);
