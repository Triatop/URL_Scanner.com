import main
import csv
import json
import func_timeout
import threading
import os
import time
import pandas as pd
theVals = []


data = ["Site","FavIcon","SecureProtocol","CheckPort","SiteAge","SiteLength","SpecialCharacters","Certificate","Malicious Links","Swapped","Pulse Count","Malicious count","IsSafe"]


def extention(file):
    return os.path.splitext(file)[-1].lower()

def loadData(file, ext):
    if ext == '.csv':
        return pd.read_csv(file)

    if ext == '.json':
        with open(file, 'r') as f:
            return json.load(f)
theFile = 'bad.csv'
ext = extention(theFile)
jsonData = loadData(theFile, ext) 
if ext == '.json':
    keysList = list(jsonData)
    valueList = list(jsonData.values())
if ext == '.csv':
    keysList = list(jsonData['Site'])
    valueList = list(jsonData['IsSafe'])


def processData(start, steps):
        for i in range(start, start+steps):
            try:
                time.sleep(2)
                val = {'Site' : keysList[i]}
                # val.update(func_timeout.func_timeout(30, main.main, (keysList[i],'admin', False)))
                val.update(main.main(keysList[i],'admin', False))
                val['IsSafe'] = (0 if valueList[i] == False else 1)
                if('valid' not in val):
                    print(val)
                    theVals.append(val.values())
            except:
                print(keysList[i], "Not working")
                pass



def makeWorkers():
    workers = 1
    while len(jsonData)%workers != 0:
        workers -= 1
    return workers

def startThreads():
    workers = makeWorkers()
    threads = []
    #length = int(len(jsonData)/workers)
    length = 20
    currVal = 7
    #CurrVal = 0, bord läggas till 1 när denna är klar
    for i in range(workers):
        threads.append(threading.Thread(target=processData, args=(currVal*length,length)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

startThreads()


with open('fixedGood.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    writer.writerows(theVals)

