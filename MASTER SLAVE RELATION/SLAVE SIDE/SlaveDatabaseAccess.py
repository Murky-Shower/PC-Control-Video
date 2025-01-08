import firebase_admin
from firebase_admin import credentials, storage, db
import json
import os
import codecs
from datetime import date

class SlaveDatabaseAccess():
    def __init__(self) -> None:
        self.scriptPath = str(os.path.dirname(os.path.realpath(__file__)))
        self.appInitialized = False
        self.acquireCredentials()

        self.ref = db.reference()

        pass

    def acquireCredentials(self):
        cred = credentials.Certificate(self.scriptPath + "\\JSON FILES\\equipeclp-firebase-adminsdk-hw94m-39723b7582.json")
        firebase_admin.initialize_app(cred, {'databaseURL': "https://equipeclp-default-rtdb.europe-west1.firebasedatabase.app/"})
        self.appInitialized = True
        pass
    
    def downloadImage(self, operationType : str = "download"):
        dateVariable = ""
        if operationType == "backup":
            today = date.today()
            year = str(today.year)
            month = str(today.month)
            day = str(today.day)
            if int(day) < 10:
                day = str(0) + day
            if int(month)<10:
                month = str(0) + month
            dateVariable = day + month + year
        databaseImage : tuple = self.ref.get()
        with codecs.open(self.scriptPath + "\\JSON FILES\\databaseImage" + dateVariable + ".json", 'w', encoding='utf-8') as f:
            json.dump(databaseImage, f, ensure_ascii=False, indent=4)

        print('DONE DOWNLOADING')
        pass
#JsonUploadFirebase().upload()