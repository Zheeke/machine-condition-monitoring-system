# machine-condition-monitoring-system 
## 1. Project Overview
This project is a real-time machine condition monitoring system that collects data from sensors mounted on machines on a production line, sends the data to a central database, and analyzes it to detect anomalies. I will simulate data collection for a single machine (machine1) and perform preliminary data analysis to identify potential problems.


## 2. Tools and Technologies Used
Programming Languages: Python
Database: SQL Server(since I’m familiar with it and it is very beginner friendly)
Data Analysis: matplotlib
Automation: Python script to simulate data collection and storage
Database Schema
I will create a machine-monitoring database with a table machine_data that stores the following columns:
ID: Unique identifier for each record
Time: Timestamp of the data record
Temperature: Temperature reading from the sensor (°C) Optimal: 
Pressure: Pressure reading from the sensor (hPa) Optimal:
Humidity: Air humidity reading from the sensor (%) Optimal:
Machine_Work: Whether machine works or not (Yes/No)

## 3. Implementation
Since, it is a simulation of a real-time machine condition monitoring system, I used random data for the project, but I decided to separate sensor data (temperature, humidity, pressure) in “sensor_reading.py” and other values generation( time and machine work state) in “data_insertion.py” script. I believe if I were to run such a project in real life, there wouldn’t be a need of time and machine work state values generation. Therefore, it would be easier to adjust the scripts. Also, personally, I think it increases readability of my code.
For “data_insertion.py” script first, I need to install pyodbc module. “pyodbc” is a Python open-source module that simplifies access to ODBC databases such as mine. Also, I need to use datetime and timedelta functions from datetime module, but it is already preinstalled. 

## 4. Data Analysis
I first ensure connection to the database. Then load data to pandas DataFrame and define optimal operating ranges

## 5. Data Visualisation
Using matplotlib packages for visualisation I will create 3 graphs: Temperature over time, Humidity over time, Pressure over time

## Result
![Humidity](https://github.com/user-attachments/assets/60ee3b56-b441-4567-b403-07be1a43e1f7)
![Pressure](https://github.com/user-attachments/assets/96f53ee7-649f-4a5d-ae4f-9cc5f6a61c83)
![Temperature](https://github.com/user-attachments/assets/9f77fb14-2c3f-43be-8914-ac681f9bdf78)
