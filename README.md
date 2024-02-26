# SwissMeteoStationsDB

In this repository, you'll find two Python scripts that fetch weather data from JSON and CSV files, storing it in an SQLite3 database. The scripts generate a view combining data from IMIS and SMN (VQHA80 & VQHA98) stations and another view with a summary of the data, allowing for calculations like total snowfall in the last hours or days.

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
