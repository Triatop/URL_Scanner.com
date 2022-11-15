import main
import csv
import json



data = ["FavIcon", "SecureProtocol", "CheckPort", "SiteAge", "SiteLength", "IsPhishy"]

with open('api/testingData.json', 'r') as f:
    jsonData = json.load(f)

with open('api/example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    for key in jsonData:
        val = main.main(key, report=False)
        val['IsPhishy'] = (0 if jsonData[key] == False else 1)
        writer.writerow(val.values())