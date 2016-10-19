import shutil
import os

###change the path source and destination
###to the applicable folders on your system
source = ("C:/Users/jmvan/Desktop/Folder A/")
sourceFiles = os.listdir(source)
destination = ("C:/Users/jmvan/Desktop/Folder B/")
def cleanUp():
    for file in sourceFiles:
        if file.endswith(".txt"):
            shutil.copy(source + file,destination)
            print (file)
            os.remove(source + file)

if __name__=='__main__':
    cleanUp()

