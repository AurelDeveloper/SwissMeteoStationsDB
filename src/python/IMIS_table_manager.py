import requests
import sqlite3
from datetime import datetime

url = 'https://measurement-api.slf.ch/public/api/imis/measurements-precipitation'

response = requests.get(url)
data = response.json()

latest_entries = {}

for item in data:
    station_code = item['station_code']
    measure_date = datetime.strptime(item['measure_date'], '%Y-%m-%dT%H:%M:%SZ')

    if station_code not in latest_entries or measure_date > datetime.strptime(latest_entries[station_code]['measure_date'], '%Y-%m-%dT%H:%M:%SZ'):
        latest_entries[station_code] = item

conn = sqlite3.connect('snowdata.db')
c = conn.cursor()

for station_code, entry in latest_entries.items():
    c.execute("INSERT INTO IMIS (station_code, measure_date, RR_10MIN_SUM) VALUES (?, ?, ?)",
              (entry['station_code'], entry['measure_date'], entry['RR_10MIN_SUM']))

conn.commit()

conn.close()