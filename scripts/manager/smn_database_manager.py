import pandas as pd
import requests
import sqlite3


def download_csv(url='https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv', file_name='smn.csv'):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)


def read_csv_data(file_path):
    df = pd.read_csv(file_path, delimiter=';', usecols=['Station/Location', 'rre150z0'])
    data = [(row['Station/Location'], row['rre150z0']) for index, row in df.iterrows()]
    return data


def create_sqlite_table(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stations
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT, rre150z0 TEXT)''')
    conn.commit()
    conn.close()


def insert_into_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO Stations (location, rre150z0) VALUES (?, ?)', data)
    conn.commit()
    conn.close()


db_path = '../smn.db'
csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'
download_csv(url=csv_url)
create_sqlite_table(db_path)
file_path = '../smn.csv'
data = read_csv_data(file_path)
insert_into_sqlite(data, db_path)
