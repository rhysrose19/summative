import random
import csv
from datetime import datetime

transducerData = []
def sensoDataGen(list = []):
    global transducerData
    for i in range(32): # create a list with nested lists of the 32 transducers
        transducerData.append([])
        for n in range(16):
            x=random.random()
            transducerData[i].append(x) # fills nested lists with 16 sensor data
    return transducerData

data = sensoDataGen(transducerData)

#Write data to a CSV file

today = datetime.today()
file = open('sensorData.csv','a') #open file for writing
writer = csv.writer(file)
writer.writerow(["date time", "sensorData"])
writer.writerow([today,data])
