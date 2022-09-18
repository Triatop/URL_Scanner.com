import URL_Object as urlObject
import UrlController as urlCtr
from flask import Flask, request



app = Flask(__name__)


@app.route('/backendAPI')
def members():

    url = urlObject.URL(request.args.get('url'))
    ctr = urlCtr.UrlController()
    urlOb = urlObject.URL_Object()
    urlOb.setURL(url)

    if not ctr.validateUrl(urlOb.getURL().u_URL):
        return "Not a valid webiste or is down"

    return "Is a valid website"




if __name__ == '__main__':
    app.run(debug=True, port=5000)