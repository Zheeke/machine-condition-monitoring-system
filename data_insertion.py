import pyodbc
from datetime import datetime, timedelta
import random
from sensor_reading import read_temperature, read_pressure, read_humidity

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R455QB9\MSSQLSERVERV16;'
    'DATABASE=machine-monitoring;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Function to generate data and insert into the database
def generate_and_insert_data(num_records):
    base_time = datetime.now()
    data = []
    for i in range(num_records):
        time = (base_time + timedelta(minutes=5 * i)).strftime('%Y-%m-%d %H:%M:%S')
        temperature = read_temperature()
        pressure = read_pressure()
        humidity = read_humidity()
        machine_work = random.choice(['Yes', 'No'])
        data.append((time, temperature, pressure, humidity, machine_work))
    
    insert_query = '''
    INSERT INTO machine_data (Time, Temperature, Pressure, Humidity, Machine_Work)
    VALUES (?, ?, ?, ?, ?)
    '''
    cursor.executemany(insert_query, data)
    conn.commit()

# Generate and insert 100 records
generate_and_insert_data(100)
conn.close()
