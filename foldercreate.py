import os
from pathlib import Path
import shutil

directoryOE = "Z:/Users/zetsuzen/Documents/SchoolActivities/Python/OOP-and-CISCO-OOP_Dump/OE/"
directoryLA = "Z:/Users/zetsuzen/Documents/SchoolActivities/Python/OOP-and-CISCO-OOP_Dump/LA/"

def create_folder(directory):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if (os.path.isfile(path) and file != "foldercreate.py"):
            directoryName = file[0:-3]
            directoryNameandFile = os.path.join(directory, directoryName)
            moveDirectory = os.path.join(directoryNameandFile, file)
            Path(directoryName).mkdir()
            shutil.move(path, moveDirectory)

def rename_folder(directory):
    for folder in os.listdir(directory):
        path = os.path.join(directory, folder)
        if os.path.isdir(path):
            foldername = folder[3:]
            newfoldername = os.path.join(directory, foldername)
            os.rename(path, newfoldername)

create_folder(directoryLA)
create_folder(directoryOE)

rename_folder(directoryLA)
rename_folder(directoryOE)