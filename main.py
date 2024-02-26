import subprocess
import sqlite3
import time

imis_path = './src/python/IMIS.py'
smn_path = "./src/python/SMN.py"

while True:

    subprocess.call(["python", imis_path])

    subprocess.call(["python", smn_path])

    conn = sqlite3.connect('meteo.db')
    c = conn.cursor()

    with open('view.sql', 'r') as sql_file:
        sql_code = sql_file.read()

    c.executescript(sql_code)

    conn.commit()
    conn.close()

    time.sleep(600)