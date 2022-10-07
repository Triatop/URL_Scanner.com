import URL_Object as urlObject
import UrlController as urlCtr
from flask import Flask, request
import webscraper



app = Flask(__name__)


@app.route('/backendAPI')
def members():
    attributeDict = main(request.args.get('url'))
    if attributeDict["valid"] != True:
        report = "- Invalid URL, website does not exist - check for spelling errors"
        return {"valid": str(attributeDict["valid"]), "report": report}

    report = ""
    for i in range(1,3):
        if i == 1:
            report += (f"- Website has favicon ({'True' if attributeDict[1] == 1 else 'False'})")
        if i == 2:
            report += (f"\n- Website uses ({attributeDict[2]}) protocol")
    return {"valid": str(attributeDict["valid"]), "report": report}

def main(url):
    ctr = urlCtr.UrlController()
    valid = ctr.validateUrl(url)
    if not valid:
        return {'valid': str(valid)}
    #Continue
    scraper = webscraper.Webscraper(url)

    favIcon = scraper.isExistFavicon()
    protocol = scraper.exfiltrateProtocol()

    return {'valid' : valid, 1 : favIcon, 2 : protocol}



if __name__ == '__main__':
    app.run(debug=True, port=8000)