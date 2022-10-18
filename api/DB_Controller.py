class DBController:
    def __init__(self):
        pass
    def storeData():            #Store user scan
        pass
    def getData(UserID):        #get scans ? (report)
        pass
    def getUserRights(UserID):     #getUserData
        pass
    def __del__(self):
        if self.connection != None:
                self.connection.close()