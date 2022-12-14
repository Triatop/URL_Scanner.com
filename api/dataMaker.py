import main
import csv
import json
import threading
import os
import time
import pandas as pd

def extention(file):
    return os.path.splitext(file)[-1].lower()

def loadData(file, ext):
    if ext == '.csv':
        return pd.read_csv(file)

    if ext == '.json':
        with open(file, 'r') as f:
            return json.load(f)

def getValues(data, ext):
    if ext == '.json':
        keysList = list(data)
        valueList = list(data.values()) 
    if ext == '.csv':
        keysList = list(data['Site'])
        valueList = list(data['IsSafe'])
    return keysList, valueList

def processData(start, steps, keysList, valueList, theVals):
        for i in range(start, start+steps):
            try:
                time.sleep(2)
                val = {'Site' : keysList[i]}
                val.update(main.main(keysList[i],'admin', False))
                val['IsSafe'] = (0 if valueList[i] == False else 1)
                if('valid' not in val):
                    print(val)
                    theVals.append(val.values())
            except:
                print(keysList[i], "Not working")
                continue



def makeWorkers(data):
    workers = 1
    while len(data)%workers != 0:
        workers -= 1
    return workers

def startThreads(data, vals, theAttributes):

    workers = makeWorkers(data)
    threads = []
    length = 5
    currVal = 0
    for i in range(workers):
        threads.append(threading.Thread(target=processData, args=(currVal*length,length, vals[0], vals[1], theAttributes)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def mainFunc():
    firstLine = ["Site","FavIcon","SecureProtocol","CheckPort","SiteAge","SiteLength","SpecialCharacters","Certificate","Malicious Links","Swapped","Pulse Count","Malicious count","IsSafe"]

    theFile = 'example.csv'
    ext = extention(theFile)
    data = loadData(theFile, ext)
    values = getValues(data, ext)
    theAttributes = []


    startThreads(data, values, theAttributes)

    with open('yes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(firstLine)
        writer.writerows(theAttributes)

if __name__ == '__main__':
    mainFunc()