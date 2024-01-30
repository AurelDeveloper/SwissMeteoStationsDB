-- VQHA98_database_schema.sql
CREATE TABLE IF NOT EXISTS VQHA98
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    date     DATETIME,
    rre150z0 FLOAT,

    CONSTRAINT location_date UNIQUE (location, date)

);
