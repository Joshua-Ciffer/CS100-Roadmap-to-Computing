"""
Joshua Ciffer
CS 100 029 HW12
November 26th, 2019
"""

#1
def safeOpen(fileName):
    try:
        return open(fileName)
    except:
        return None

#2
def safeFloat(x):
    try:
        return float(x)
    except:
        return 0.0

#3
def averageSpeed():
    fileName = input('Enter the input file: ')
    file = safeOpen(fileName)
    if file == None:
        print('File not found, try again.')
        fileName = input('Enter the input file: ')
        file = safeOpen(fileName)
        if file == None:
            print('File not found, program exiting.')
            exit()
    average = 0.0
    i = 0
    for line in file:
        x = safeFloat(line)
        if x > 2:
           i += 1
            average += x
    average /= i
    print('Average speed is ' + str(average) + ' mph.')