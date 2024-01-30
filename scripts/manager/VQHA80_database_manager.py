import pandas as pd
import requests
import sqlite3

def download_csv(url='https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv', file_name='smn.csv'):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

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

def read_csv_data(file_path):
    df = pd.read_csv(file_path, delimiter=';', usecols=['Station/Location', 'rre150z0', 'Date'])
    df['rre150z0'] = pd.to_numeric(df['rre150z0'], errors='coerce')
    data = [(row['Station/Location'], row['rre150z0'], row['Date']) for index, row in df.iterrows()]
    return data

def insert_into_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO Stations (location, rre150z0, date) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

db_path = '../VQHA80.db'
csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'
download_csv(url=csv_url)

schema_path = 'schema.sql'
schema = read_sql_schema(schema_path)

create_sqlite_table(db_path, schema)

file_path = '../data/VQHA80.csv'
data = read_csv_data(file_path)
insert_into_sqlite(data, db_path)
