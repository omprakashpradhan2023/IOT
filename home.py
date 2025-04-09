import sqlite3
import random
import time

# Setup database
conn = sqlite3.connect('home_data.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS readings (
        timestamp TEXT,
        temperature REAL,
        humidity REAL
    )
''')
conn.commit()

# Function to simulate reading sensor
def read_sensor():
    temp = random.uniform(20, 40)  # fake temperature
    hum = random.uniform(30, 70)   # fake humidity
    return temp, hum

# Function to insert data into DB
def save_to_db(temp, hum):
    cursor.execute("INSERT INTO readings VALUES (datetime('now'), ?, ?)", (temp, hum))
    conn.commit()

# Function to check for alert
def check_alert(temp):
    if temp > 30:
        print(f"🚨 ALERT: High temperature: {temp:.2f}°C")
    else:
        print(f"✅ Temperature is OK: {temp:.2f}°C")

# Main loop
while True:
    temperature, humidity = read_sensor()
    save_to_db(temperature, humidity)
    check_alert(temperature)
    print(f"Saved: Temp={temperature:.2f}°C, Humidity={humidity:.2f}%")
    time.sleep(5)  # wait 5 seconds before next reading
