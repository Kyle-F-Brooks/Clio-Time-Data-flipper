import os
import shutil

def flippedNames(degreesOfSeperation):
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

def invertedNames(degreesOfSeperation):
    newNames = []
    array1 = []
    array2 = []
    m = 0
    while m <= 180: #loop for first half
        p = 180
        while p >= 0: # count parallels backwars as they get inversed later
            array1.append("IR %s %s.txt" % ((m*100), (p*100)))
            p -= degreesOfSeperation
        m += degreesOfSeperation
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

def copy_and_rename(src_path, dest_path, new_name):
    # Copy and rename the file
    new_path = f"{dest_path}/{new_name}"
    shutil.copy(src_path, new_path)

def rename_files(inputPath, outputPath, originalNames, newNames):
    # iterate over files in directory
    for filename in os.listdir(inputPath):
        # if numOfFiles < 180:
        f = os.path.join(inputPath, filename)
        # checking if it is a file
        print(filename)
        for i,j in enumerate(originalNames):
            if j==filename:
                print(j)
                if os.path.isfile(f):
                    copy_and_rename(os.path.abspath(f), outputPath, newNames[i])
            # print(os.path.abspath(f))
        # elif numOfFiles == 180:
        #     f = os.path.join(inputPath, filename)
        #     # checking if it is a file
        #     if os.path.isfile(f):
        #         copy_and_rename(os.path.abspath(f), outputPath, newNames[numOfFiles])
        #     numOfFiles += 1
        # elif numOfFiles > 180:
        #     f = os.path.join(inputPath, filename)
        #     # checking if it is a file
        #     if os.path.isfile(f):
        #         copy_and_rename(os.path.abspath(f), outputPath, newNames[numOfFiles])
        #     numOfFiles += 1

inputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Test Data"
outputPath = "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Output Data"
originalOrder = os.listdir(inputPath)
# print (len(dirList))
# names = createNewFileNames()
names = invertedNames(degreesOfSeperation=5)
# file = open("test.txt", "w+")
# file.write(str(names))
# file.close()
print(len(originalOrder))
print(len(names))

# copy_and_rename("C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//test.txt", "C://Users//Kyle//Documents//Scripts//Clio Time Data flipper//Output Data", "jeff.txt")
rename_files(inputPath, outputPath, originalOrder, names)
