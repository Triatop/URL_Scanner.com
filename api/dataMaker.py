import main
import csv
import json
import func_timeout
import threading

theVals = []


data = ["Site","FavIcon", "SecureProtocol", "CheckPort", "SiteAge", "SiteLength", "SpecialCharacters", "Certificate", "Malicious Links", "IsSafe"]

def loadData(file):
    with open(file, 'r') as f:
        return json.load(f)

jsonData = loadData('theData.json') 

def processData(start, steps):

        keysList = list(jsonData)
        valueList = list(jsonData.values())

        for i in range(start, start+steps):
            try:
                val = {'Site' : keysList[i]}
                val.update(func_timeout.func_timeout(30, main.main, (keysList[i], False)))
                val['IsSafe'] = (0 if valueList[i] == False else 1)
                if('valid' not in val):
                    #a += val.values()
                    #writer.writerow(val.values())
                    print(val)
                    theVals.append(val.values())
            except:
                pass



def makeWorkers():
    workers = 50
    while len(data)%workers != 0:
        workers -= 1
    return workers

def startThreads():
    workers = makeWorkers()
    threads = []
    length = int(len(jsonData)/workers)
    for i in range(workers):
        threads.append(threading.Thread(target=processData, args=(i*length,length)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

startThreads()

with open('good.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    writer.writerows(theVals)

