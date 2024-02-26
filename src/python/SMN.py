import pandas as pd
import requests
import sqlite3
from io import StringIO

from config import SNOWDATA_SQLITE

def download_csv(url):
    response = requests.get(url)
    csv_data = response.text
    return csv_data

def read_sql_schema(file_path):
    with open(file_path, 'r') as file:
        schema = file.read()
    return schema

def create_sqlite_table(db_path, schema):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)

def read_csv_data(csv_data):
    df = pd.read_csv(StringIO(csv_data), delimiter=';', usecols=['Station/Location', 'Date', 'tre200s0', 'rre150z0', 'sre000z0', 'gre000z0', 'ure200s0', 'tde200s0', 'dkl010z0', 'fu3010z0', 'fu3010z1', 'prestas0', 'pp0qffs0', 'pp0qnhs0', 'ppz850s0', 'ppz700s0', 'dv1towz0', 'fu3towz0', 'fu3towz1', 'ta1tows0', 'uretows0', 'tdetows0'])
    data = [(row['Station/Location'], row['Date'], row['tre200s0'], row['rre150z0'], row['sre000z0'], row['gre000z0'], row['ure200s0'], row['tde200s0'], row['dkl010z0'], row['fu3010z0'], row['fu3010z1'], row['prestas0'], row['pp0qffs0'], row['pp0qnhs0'], row['ppz850s0'], row['ppz700s0'], row['dv1towz0'], row['fu3towz0'], row['fu3towz1'], row['ta1tows0'], row['uretows0'], row['tdetows0']) for _, row in df.iterrows()]
    return data

def insert_into_sqlite(data, db_path, table_name):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executemany(f'INSERT INTO {table_name} (location, date, tre200s0, rre150z0, sre000z0, gre000z0, ure200s0, tde200s0, dkl010z0, fu3010z0, fu3010z1, prestas0, pp0qffs0, pp0qnhs0, ppz850s0, ppz700s0, dv1towz0, fu3towz0, fu3towz1, ta1tows0, uretows0, tdetows0) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)

def is_duplicate_data(db_path, table_name, csv_date):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT max( date ) FROM {table_name};')
        max_data = cursor.fetchone()[0]
        print(max_data, csv_date)
        return max_data == csv_date

def main(csv_url, db_path, schema_path, table_name):
    csv_data = download_csv(url=csv_url)

    schema = read_sql_schema(schema_path)
    create_sqlite_table(db_path, schema)

    data = read_csv_data(csv_data)

    csv_date = data[1][1]

    if is_duplicate_data(db_path, table_name, csv_date):
        print("Daten sind bereits aktuell. Keine Einfügeoperation durchgeführt.")
        exit(0)

    non_duplicate_data = [(location, date, rre150z0) for location, date, rre150z0 in data if (location, date)]

    insert_into_sqlite(non_duplicate_data, db_path, table_name)

if __name__ == "__main__":
    csv_url_vqha80 = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'
    csv_url_vqha98 = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA98.csv'
    db_path = SNOWDATA_SQLITE
    schema_path = 'src/sql/snowdata_table_schema.sql'

    main(csv_url_vqha80, db_path, schema_path, 'VQHA80')
    main(csv_url_vqha98, db_path, schema_path, 'VQHA98')
