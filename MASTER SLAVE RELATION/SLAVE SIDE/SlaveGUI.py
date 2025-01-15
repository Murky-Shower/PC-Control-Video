import SlaveDatabaseAccess as dbAccess

class SlaveGUI():
    def __init__(self):
        self.slaveDb = dbAccess.SlaveDatabaseAccess()
        pass

    def createAccount(self):
        user = input("user name \n")
        pw = input("user pw \n")
        userType = "slave"
        pass