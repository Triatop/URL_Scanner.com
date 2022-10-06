import URL_Object as urlObject
import UrlController as urlCtr
from flask import Flask, request
import webscraper



app = Flask(__name__)


@app.route('/backendAPI')
def members():
    return main(request.args.get('url'))

def main(url):
    ctr = urlCtr.UrlController()
    valid = ctr.validateUrl(url)
    if not valid:
        return {'valid': str(valid)}
    #Continue
    scraper = webscraper.Webscraper(url)

    favIcon = scraper.isExistFavicon()
    protocol = scraper.exfiltrateProtocol()

    # return {'valid' : valid, 'favIcon' : favIcon, 'protocol' : protocol}

    #------
    attributeDict = {"valid": valid, 1: "\n-Website has favicon", 2: "\n-Website uses HTTPS protocol "}
    report = ""
    for i in range(1,3):
        report += attributeDict[i]
    return {"valid": str(valid), "report": report}



if __name__ == '__main__':
    app.run(debug=True, port=8000)