import pandas as pd
import requests
import sqlite3

def download_csv(csv_url='https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv', file_name='imis.csv'):
    response = requests.get(csv_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def read_csv_data(file_path):
    df = pd.read_csv(file_path, delimiter=';',
                     usecols=['Kanton', 'KoordinatenN', 'KoordinatenE', 'Station/Location', 'Stationstyp', 'Daten seit',
                              'Stationshöhe m ü. M.', 'rre150z0'])
    data = [(row['Kanton'], row['KoordinatenN'], row['KoordinatenE'], row['Station/Location'], row['Stationstyp'],
             row['Daten seit'], row['Stationshöhe m ü. M.'], row['rre150z0']) for index, row in df.iterrows()]
    return data

def create_sqlite_table(db_path, schema_file='../schema/imis_schema.sql'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(schema_file, 'r') as schema_file:
        schema = schema_file.read()

    cursor.executescript(schema)
    conn.commit()
    conn.close()

def insert_into_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany(
        'INSERT INTO Stations (Kanton, KoordinatenN, KoordinatenE, Station, Stationstyp, Daten_seit, Stationshöhe_m_ü_M, Messungen) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_path = '../data/imis.db'
    csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'
    download_csv(csv_url, file_name='imis.csv')
    create_sqlite_table(db_path)
    data = read_csv_data(file_path='../data/imis.csv')
    insert_into_sqlite(data, db_path)
