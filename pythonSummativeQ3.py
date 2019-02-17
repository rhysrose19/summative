import random
import logging
#create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "error_file.log" ,
                    level = logging.ERROR,
                    format = LOG_FORMAT,
                    )
logger = logging.getLogger()

#Test the logger
logger.info("Our first message")

transducerData = []
def sensorDataGen(list = []):
    '''Generate corrupt dataset for 32 transducers each with 16 sensor readings.

    The data is in a list of list mixed in float and strings data type'''
    global transducerData
    for i in range(32):             # create a list with nested lists of the 32 transducers
        transducerData.append([])
        for n in range(16):         # fills nested lists with 16 sensor data
            x=random.random()
            if n % 2 == 0:
                transducerData[i].append(x)
            else: transducerData[i].append('err') #corrupt the data by replacing one entry with "err"
    return transducerData

data = sensorDataGen(transducerData) #corrupt data set
#dataset= tuple(data)
print(data)
print(sensorDataGen.__doc__)

#function to check for errors in data set
def checkData(to_search, target):
    ''' serches the data set and finds index of the corrupt data.

    It takes both the data set and target error as input.'''
    ntransducer = 0
    for i in to_search:
        ntransducer += 1
        for j, value in enumerate(i):
            if value == target:
                logger.error("error found")

checkData(data, 'err')

