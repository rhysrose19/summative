import random
transducerData = []
def sensorDataGen(list = []):
    ''' Generate dummy sensor data for 32 transducers each listing 16 sensor readings.

    The data is in a list of list and type is float between o and 1'''
    global transducerData
    for i in range(32): # create a list with nested lists of the 32 transducers
        transducerData.append([])
        for n in range(16):
            x=random.random()
            transducerData[i].append(x) # fills nested lists with 16 sensor data
    return transducerData

data = sensorDataGen(transducerData) #generate 512 sensor readings
dataSet= tuple(data) #change data to immutable format
print("The sensor data for all {} transducers is {}" .format(len(data), data))
print(sensorDataGen.__doc__)





