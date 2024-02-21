# SwissSnowFinderDB

Welcome to the SwissSnowFinderDB project! This Python and SQL initiative focuses on extracting CSV and JSON data, storing it in a database, and using SQL to connect ski stations with nearby weather stations. The algorithm determines optimal snow conditions for users and creates an API to send the optimal snow conditions to the App.

## Features ⚙️

- **Data Retrieval**: Extracting CSV and JSON data from URLs.
- **Database Integration**: Efficient storage in an SQLite3 database.
- **SQL Linkages**: Connecting ski stations with nearby weather stations for precise information.

## ToDo 📋

- **Optimal Conditions Algorithm**: Determining the best snow conditions based on various factors.
- **App Notifications**: Users receive notifications about upcoming optimal ski conditions on their App.

**⛔️(The app will be developed in another repository)**

## Data source 💾

**JSON:**
- IMIS Weather Station: [`IMIS Measurements Precipitation`](https://measurement-api.slf.ch/public/api/imis/measurements-precipitation)

**CSV:**
- VQHA80 Weather Station: [`VQHA80 Measurements`](https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv)
- VQHA98 Weather Station: [`VQHA98 Measurements`](https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA98.csv)

## Technologie 📟

- `SQLite3`
- `Python`
- `pandas`

