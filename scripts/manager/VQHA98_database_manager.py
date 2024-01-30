import pandas as pd
import requests
import sqlite3
from io import StringIO

def download_csv(url='https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA98.csv'):
    response = requests.get(url)
    csv_data = response.text
    return csv_data

def read_sql_schema(file_path='schema.sql'):
    with open(file_path, 'r') as file:
        schema = file.read()
    return schema

def create_sqlite_table(db_path, schema):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def read_csv_data(csv_data):
    df = pd.read_csv(StringIO(csv_data), delimiter=';', usecols=['Station/Location', 'Date', 'rre150z0'])
    data = [(row['Station/Location'], row['Date'], row['rre150z0']) for index, row in df.iterrows()]
    return data

def insert_into_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO VQHA98 (location, date, rre150z0) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()


csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA98.csv'
csv_data = download_csv(url=csv_url)

db_path = '../../deine_datenbank.db'
schema_path = '../../schema/VQHA98_database_schema.sql'

schema = read_sql_schema(schema_path)
create_sqlite_table(db_path, schema)

data = read_csv_data(csv_data)
insert_into_sqlite(data, db_path)
