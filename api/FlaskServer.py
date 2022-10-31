import URL_Object as urlObject
import UrlController as urlCtr
import PortCheck
from flask import Flask, request
import webscraper
import time
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/backendAPI')
def members():
    sTime = time.time()
    attributeDict = main(request.args.get('url'))
    if attributeDict["valid"] != True:
        report = "- Invalid URL, website does not exist - check for spelling errors"
        return {"valid": str(attributeDict["valid"]), "report": report}

    report = ""
    for i in range(1,5):
        if i == 1:
            report += (f"- Website has {'a' if attributeDict[i] == 1 else 'no'} favicon ")
        if i == 2:
            report += (f"\n- Website uses {attributeDict[i].upper()} protocol")
        if i == 3:
            report += (f"\n- Website is running on the {'right' if attributeDict[i] == True else 'wrong'}  port")
        if i == 4:
            report += (f"\n- The age of the webiste is {attributeDict[i]}")
    return {"valid": str(attributeDict["valid"]), "report": report, "exeTime": f'The scan took {(time.time() - sTime):.2f} seconds'}


def main(url):
    ctr = urlCtr.UrlController()
    ip = ctr.validateUrl(url)
    if not ip:
        return {'valid': False}
    #Continue
    scraper = webscraper.Webscraper(url)
    portCheck = PortCheck.PortCheck()
    



    favIcon = scraper.isExistFavicon()
    protocol = scraper.exfiltrateProtocol()
    age = scraper.exfiltrateSiteAge()
    port = portCheck.checkPorts(ip, protocol)

    return {'valid' : True, 1 : favIcon, 2 : protocol, 3 : port, 4 : age}



if __name__ == '__main__':
    app.run(debug=True, port=8000)