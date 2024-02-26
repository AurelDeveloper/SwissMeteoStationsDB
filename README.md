# SwissMeteoStationsDB

In this repository, you'll find two Python scripts that fetch weather data from JSON and CSV files, storing it in an SQLite3 database. The scripts generate a view combining data from IMIS and SMN (VQHA80 & VQHA98) stations and another view with a summary of the data, allowing for calculations like total snowfall in the last hours or days.

## Let's Get Started 🚀
1. Install the required packages using the following command:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Initialize the SQLite database:
   ```bash
   sqlite3 meteo.db
   ```

3. Create the "VQHA80" table with the following SQL command:
   ```sql
   ```sql
   CREATE TABLE IF NOT EXISTS VQHA80 (
       id       INTEGER PRIMARY KEY AUTOINCREMENT,
       location TEXT,
       rre150z0 FLOAT,
       date     DATETIME,
       CONSTRAINT location_date UNIQUE (location, date)
   );
   ```

4. Create the "VQHA98" table with the following SQL command:
   ```sql
   CREATE TABLE IF NOT EXISTS VQHA98 (
       id       INTEGER PRIMARY KEY AUTOINCREMENT,
       location TEXT,
       date     DATETIME,
       rre150z0 FLOAT,
       CONSTRAINT location_date UNIQUE (location, date)
   );
   ```

5. Create the "IMIS" table with the following SQL command:
   ```sql
   CREATE TABLE IF NOT EXISTS IMIS (
       id           INTEGER PRIMARY KEY AUTOINCREMENT,
       station_code TEXT,
       measure_date DATETIME,
       RR_10MIN_SUM FLOAT
   );
   ```

## Features ⚙️

- **Data Retrieval**: Extracting CSV and JSON data from URLs.
- **Database Integration**: Efficient storage in an SQLite3 database.
- **Combine Data**: Merge SMN and IMIS stations' weather data and generate another view with a time summary of the weather database.

## Data source 💾

**JSON:**
- IMIS Weather Station: [`IMIS Measurements Precipitation`](https://measurement-api.slf.ch/public/api/imis/measurements-precipitation)

**CSV:**
- VQHA80 Weather Station: [`VQHA80 Measurements`](https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv)
- VQHA98 Weather Station: [`VQHA98 Measurements`](https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA98.csv)

## Technology 📟

- `SQLite3`
- `Python`
- `pandas`
