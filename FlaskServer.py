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
        return {'valid': valid}
    #Continue
    scraper = webscraper.Webscraper(url)

    favIcon = scraper.isExistFavicon()

    return {'valid' : valid, 'favIcon' : favIcon}


if __name__ == '__main__':
    app.run(debug=True, port=5000)