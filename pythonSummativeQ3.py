import random

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
''' 
nValue= 0

def numValue(string_data):
#Calculate the numerical value of the string.Takes a string input parameter.
    global nValue
    for i in range(len(string_data)):
        nValue += ord(string_data[i])
    return nValue

print(numValue('err'))

'''
#function to check for errors in data set
def checkData(to_search, target):
    ''' serches the data set and finds index of the corrupt data.

    It takes both the data set and target error as input.'''
    ntransducer = 0
    for i in to_search:
        ntransducer += 1
        for j, value in enumerate(i):
            if value == target: #and numValue(str(value)) == numValue(target):
                print("sensor number {}, transducer number{}".format(j,ntransducer))

checkData(data, 'err')


''' 
#takwimu=((1,2,'err'))
def find_index(to_search, target):
    Find the index of a value in a sequence
    for j in to_search:
        for i, value in enumerate(j):
            if value == target:
                print("sensor number {}".format(i))
            else:
                continue
        print("transducer {}".format(j))

index= find_index(data, 'err')
print(index)

'''
#import logging
#logging.warning('Watch out!')  # will print a message to the console
#logging.info('I told you so')  # will not print anything
