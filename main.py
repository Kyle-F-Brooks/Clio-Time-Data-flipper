import os
import shutil

def normalNames(degreesOfSeperation):
    newNames = [] # empty array for new file names
    m = 0
    while m <= 360:
        p = 0
        while  p <= 180:
            newNames.append("IR %s %s.txt" % ((m*100), (p*100)))
            p += degreesOfSeperation
        m += degreesOfSeperation

    return newNames

def invertedNames(degreesOfSeperation):
    # Creates an inverted list of original data. Parallels do not get inverted
    newNames = [] # declare returned variable
    array1 = []# first half
    array2 = []# second half
    m = 0 # set the meridian degree
    while m <= 180: #loop for first half
        p = 180 # set parallel degree
        while p >= 0: # count parallels backwars as they get inversed later
            array1.append("IR %s %s.txt" % ((m*100), (p*100)))
            p -= degreesOfSeperation # count down parallels by degrees of seperation
        m += degreesOfSeperation # count up meridians by degrees of seperation
    if m >= 180: #loop for second half
        while m <= 360:
            p = 180
            while p >= 0:
                array2.append("IR %s %s.txt" % ((m*100), (p*100)))
                p -= degreesOfSeperation
            m += degreesOfSeperation
    yarra1 = list(reversed(array1)) # inverse the list
    yarra2 = list(reversed(array2))
    # stick the lists together
    for x in yarra1:
        newNames.append(x)
    for x in yarra2:
        newNames.append(x)
    return newNames

def copyRename(src_path, dest_path, new_name):
    # Copy and rename the file
    new_path = f"{dest_path}/{new_name}"
    shutil.copy(src_path, new_path)

def processFiles(inputPath, outputPath, originalNames, newNames):
    # iterate over files in directory
    for i,j in enumerate(originalNames): # i = key, j = value
        for filename in os.listdir(inputPath): 
            f = os.path.join(inputPath, filename)
            if j==filename:
                if os.path.isfile(f):
                    copyRename(os.path.abspath(f), outputPath, newNames[i])
# Set user variables
inputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Input Data"
outputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Output Data"
degrees = 5 # degrees between measurements

correctOrder = normalNames(degrees) # create list of original order
names = invertedNames(degrees) # create an inverted order

processFiles(inputPath, outputPath, correctOrder, names) # copy and rename files