-- VQHA80
CREATE TABLE IF NOT EXISTS VQHA80 (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    rre150z0 FLOAT,
    date     DATETIME,
    CONSTRAINT location_date UNIQUE (location, date)
);

-- VQHA98
CREATE TABLE IF NOT EXISTS VQHA98 (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT,
    date     DATETIME,
    rre150z0 FLOAT,
    CONSTRAINT location_date UNIQUE (location, date)
);

-- IMIS
CREATE TABLE IF NOT EXISTS IMIS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_code TEXT,
    measure_date DATETIME,
    RR_10MIN_SUM FLOAT,
);

-- ski_stations
CREATE TABLE IF NOT EXISTS ski_stations (
     id INTEGER PRIMARY KEY,
     name TEXT,
);

-- weather_stations
CREATE TABLE IF NOT EXISTS weather_stations(
     id INTEGER PRIMARY KEY

);

-- many-to-many between ski stations and weather stations
CREATE TABLE IF NOT EXISTS ski_weather_stations (
     ski_station_id     INTEGER,
     weather_station_id INTEGER,
     PRIMARY KEY (ski_station_id, weather_station_id),
     FOREIGN KEY (ski_station_id) REFERENCES ski_stations (id),
     FOREIGN KEY (weather_station_id) REFERENCES weather_stations (id)
);
