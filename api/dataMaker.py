import main
import csv
import json
import func_timeout



data = ["Site","FavIcon", "SecureProtocol", "CheckPort", "SiteAge", "SiteLength", "IsSafe"]

with open('badData.json', 'r') as f:
    jsonData = json.load(f)

with open('bad2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    for key in jsonData:
        try:
            print(key)
            val = {'Site' : key}
            val.update(func_timeout.func_timeout(30, main.main, (key, False)))
            val['IsSafe'] = (0 if jsonData[key] == False else 1)
            if('valid' not in val):
                print(val)
                writer.writerow(val.values())
        except:
            pass