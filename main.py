from os import listdir
# from os.path import isfile, join

myPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Test Data"
dirList = listdir(myPath)

def createNewFileNames():
    degreesOfSeperation = 5 # Set the degree seperation of each measurement
    newNames = []
    currentDegree = 0
    while currentDegree <= 360:
        currentDegree += degreesOfSeperation



