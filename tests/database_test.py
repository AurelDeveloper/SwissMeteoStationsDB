import sqlite3

def test_sqlite_connection(database_path):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Überprüfe, ob Daten in der Tabelle "Stations" vorhanden sind.
        cursor.execute("SELECT * FROM stations")
        data = cursor.fetchall()

        if data:
            print("Daten in der Tabelle 'stations' gefunden:")
            for row in data:
                print(row)
        else:
            print("Keine Daten in der Tabelle 'stations' gefunden.")

        connection.close()

    except sqlite3.Error as error:
        print("Fehler bei der Verbindung zur SQLite-Datenbank:", error)

# Passe den Pfad zur SQLite-Datenbank entsprechend an.
database_path = "./stations.db"

# Rufe die Funktion auf, um den Test durchzuführen.
test_sqlite_connection(database_path)
