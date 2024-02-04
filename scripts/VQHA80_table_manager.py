import pandas as pd
import requests
import sqlite3
from io import StringIO

from config import SNOWDATA_SQLITE

def download_csv(url='https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'):
    response = requests.get(url)
    csv_content = response.content.decode('utf-8')
    return csv_content

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

def read_csv_data(csv_content):
    csv_file = StringIO(csv_content)
    df = pd.read_csv(csv_file, delimiter=';', usecols=['Station/Location', 'rre150z0', 'Date'])
    df['rre150z0'] = pd.to_numeric(df['rre150z0'], errors='coerce')
    data = [(row['Station/Location'], row['rre150z0'], row['Date']) for index, row in df.iterrows()]
    return data

def insert_into_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO VQHA80 (location, rre150z0, date) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

db_path = SNOWDATA_SQLITE
schema_path = 'scripts/snowdata_table_schema.sql'
csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'

csv_content = download_csv(url=csv_url)

schema = read_sql_schema(schema_path)

create_sqlite_table(db_path, schema)

data = read_csv_data(csv_content)
insert_into_sqlite(data, db_path)
