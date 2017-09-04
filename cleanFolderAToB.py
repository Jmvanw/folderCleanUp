
import shutil
import os

###change the path source and destination
###to the applicable folders on your system
def cleanUp(src, des):
    sourceFiles = os.listdir(src)
    for file in sourceFiles:
        if file.endswith(".txt"):
            shutil.copy(src + file,des)
            print (file)
            os.remove(src + file)

def main():
    src = ("C:/Users/jmvan/Desktop/A/")
    des = ("C:/Users/jmvan/Desktop/B/")
    cleanUp(src, des)

if __name__=='__main__':
    main()

    
