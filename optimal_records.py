import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R455QB9\MSSQLSERVERV16;'
    'DATABASE=machine-monitoring;'
    'Trusted_Connection=yes;'
)

# Load data from the database into a pandas DataFrame
query = 'SELECT * FROM machine_data'
df = pd.read_sql(query, conn)

# Convert 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Define optimal operating ranges
optimal_temperature_range = (20, 25)
optimal_pressure_range = (1010, 1015)
optimal_humidity_range = (30, 40)

# Identify records where the machine works properly and all conditions fall into the optimal range
optimal_records = df[
    (df['Machine_Work'] == 'Yes') &
    (df['Temperature'] >= optimal_temperature_range[0]) & (df['Temperature'] <= optimal_temperature_range[1]) &
    (df['Pressure'] >= optimal_pressure_range[0]) & (df['Pressure'] <= optimal_pressure_range[1]) &
    (df['Humidity'] >= optimal_humidity_range[0]) & (df['Humidity'] <= optimal_humidity_range[1])
]

# Print the optimal records
print("Optimal records detected:")
print(optimal_records)

# Plot temperature over time
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Temperature'], label='Temperature')
plt.axhline(y=optimal_temperature_range[0], color='r', linestyle='--', label='Optimal Range')
plt.axhline(y=optimal_temperature_range[1], color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.show()

# Plot pressure over time
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Pressure'], label='Pressure')
plt.axhline(y=optimal_pressure_range[0], color='r', linestyle='--', label='Optimal Range')
plt.axhline(y=optimal_pressure_range[1], color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Pressure (hPa)')
plt.title('Pressure Over Time')
plt.legend()
plt.show()

# Plot humidity over time
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Humidity'], label='Humidity')
plt.axhline(y=optimal_humidity_range[0], color='r', linestyle='--', label='Optimal Range')
plt.axhline(y=optimal_humidity_range[1], color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.legend()
plt.show()

conn.close()
