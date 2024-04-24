from os import listdir
import shutil

def createNewFileNames():
    degreesOfSeperation = 5 # Set the degree seperation of each measurement
    newNames = [] # empty array for new file names
    currentMeridian = 0
    m = 180
    while currentMeridian < 360:
        p = 0
        while  p <= 180:
            newNames.append("IR %s %s.txt" % ((m*100), (p*100)))
            p += degreesOfSeperation
        
        if m < 355:
            m += degreesOfSeperation
        elif m == 355:
            m = 0

        currentMeridian += degreesOfSeperation

    return newNames

def copy_and_rename(src_path, dest_path, new_name):
    # Copy and rename the file
    new_path = f"{dest_path}/{new_name}"
    shutil.copy(src_path, new_path)

inputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Test Data"
outputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Output Data"
originalOrder = listdir(inputPath)
# print (len(dirList))
# names = createNewFileNames()

# file = open("test.txt", "w+")
# file.write(str(names))
# file.close()
# copy_and_rename("C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//test.txt", "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Output Data", "jeff.txt")
