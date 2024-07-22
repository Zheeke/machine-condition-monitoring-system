import random
'''these are random values from the sensors. 
   If there was a machine with a sensors I would replace this data with the actual data, 
   but for this test case it's okay'''
def read_temperature():
    return random.uniform(18, 30) # normal is 20-25

def read_pressure():
    return random.uniform(  1005, 1020) # normal is 1010-1015

def read_humidity():
    return random.uniform(25, 50) # normal is 30-40