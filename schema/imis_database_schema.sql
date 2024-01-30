-- imis_database_schema.sql

CREATE TABLE IF NOT EXISTS Stations (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Kanton TEXT,
                                        KoordinatenN REAL,
                                        KoordinatenE REAL,
                                        Station TEXT,
                                        Stationstyp TEXT,
                                        Daten_seit TEXT,
                                        Stationshöhe_m_ü_M REAL,
                                        Messungen TEXT
);
