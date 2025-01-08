import os
import csv
import json 

from customtkinter import *
from customtkinter import filedialog

class UserData:
    def __init__(self) -> None:

        self.curDir = os.getcwd()
        userDataFileName = "user_data"

        pass 

    def initSaveFile(self):
        if not os.path.isfile(self.curDir + "\\userdata\\user_data.csv"):
            open(self.curDir + "\\userdata\\user_data.csv", "w", newline='')

    def loadUserData(self):
        with open(self.curDir+ "\\userdata\\user_data.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                userDataStorage = row


    def saveUserData(self):
        with open(self.curDir + "userdata\\save.csv", "w", newline='') as f:
            writer = csv.writer(f)
            userDataStorage = []
            writer.writerow(userDataStorage)


