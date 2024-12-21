import os
from pathlib import Path
import shutil

def list_files(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if (os.path.isfile(path) and file != "foldercreate.py"):
            directoryName = file[0:-3]
            directoryNameandFile = os.path.join(directory, directoryName)
            moveDirectory = os.path.join(directoryNameandFile, file)
            Path(directoryName).mkdir()
            shutil.move(path, moveDirectory)


directory = "Z:/Users/zetsuzen/Documents/SchoolActivities/Python/OOP-and-CISCO-OOP_Dump/"
list_files(directory)