import time
from scripts.database_manager import download_csv, create_sqlite_table, read_csv_data, insert_into_sqlite

def main():
    while True:
        db_path = 'stations.db'
        csv_url = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv'
        download_csv(url=csv_url)
        create_sqlite_table(db_path)
        file_path = 'data.csv'
        data = read_csv_data(file_path)
        insert_into_sqlite(data, db_path)

        time.sleep(300)

if __name__ == "__main__":
    main()