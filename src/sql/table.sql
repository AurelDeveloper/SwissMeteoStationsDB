CREATE TABLE IF NOT EXISTS VQHA80 (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    rre150z0 FLOAT,
    date     DATETIME,
    CONSTRAINT location_date UNIQUE (location, date)
);

CREATE TABLE IF NOT EXISTS VQHA98 (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    date     DATETIME,
    rre150z0 FLOAT,
    CONSTRAINT location_date UNIQUE (location, date)
);

CREATE TABLE IF NOT EXISTS IMIS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_code TEXT,
    measure_date DATETIME,
    RR_10MIN_SUM FLOAT
);