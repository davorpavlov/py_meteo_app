import sqlite3

def insert_weather_data(city, indoor_temp, outdoor_temp, indoor_pressure, outdoor_pressure, indoor_humidity, outdoor_humidity):
    """Ubacuje vremenske podatke u bazu"""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute("INSERT INTO weather (city, indoor_temp, outdoor_temp, indoor_pressure, outdoor_pressure, indoor_humidity, outdoor_humidity) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (city, indoor_temp, outdoor_temp, indoor_pressure, outdoor_pressure, indoor_humidity, outdoor_humidity))

    conn.commit()
    conn.close()

def create_table():
    db_connection = sqlite3.connect("weather.db")
    cursor = db_connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      city TEXT,
                      indoor_temp FLOAT,
                      outdoor_temp FLOAT,
                      indoor_pressure FLOAT,
                      outdoor_pressure FLOAT,
                      indoor_humidity FLOAT,
                      outdoor_humidity FLOAT,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    db_connection.commit()
    db_connection.close()

# create_table()
