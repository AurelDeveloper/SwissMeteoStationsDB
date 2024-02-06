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
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)

def read_csv_data(csv_content):
    df = pd.read_csv(StringIO(csv_content), delimiter=';', usecols=['Station/Location', 'rre150z0', 'Date'])
    df['rre150z0'] = pd.to_numeric(df['rre150z0'], errors='coerce')
    data = [(row['Station/Location'], row['rre150z0'], row['Date']) for _, row in df.iterrows()]
    return data

def insert_into_sqlite(data, db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO VQHA80 (location, rre150z0, date) VALUES (?, ?, ?)', data)

def check_new_data(db_path, max_date_in_db, max_date_in_csv):
    if max_date_in_db and max_date_in_db >= max_date_in_csv:
        print("No new data.")
        exit(0)

db_path = SNOWDATA_SQLITE
schema_path = 'snowdata_table_schema.sql'
csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'

csv_content = download_csv(url=csv_url)

schema = read_sql_schema(schema_path)

create_sqlite_table(db_path, schema)

sql_command = "SELECT MAX(STRFTIME('%Y-%m-%d %H:%M:%S', date)) FROM VQHA80;"
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute(sql_command)
    max_date_str = cursor.fetchone()[0]

max_date_in_db = pd.Timestamp(max_date_str) if max_date_str else None

data = read_csv_data(csv_content)
max_date_in_csv = max(data, key=lambda x: x[-1])[-1]
check_new_data(db_path, max_date_in_db, max_date_in_csv)

insert_into_sqlite(data, db_path)
