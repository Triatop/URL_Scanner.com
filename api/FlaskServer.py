import URL_Object as urlObject
import UrlController as urlCtr
import PortCheck
from flask import Flask, request
import webscraper
import time
import main as main
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/backendAPI')
def members():
    sTime = time.time()
    retDict = main.main(request.args.get('url'))
    if retDict["valid"] == "True":
        retDict["exeTime"] = f'The scan took {(time.time() - sTime):.2f} seconds'
    print(retDict)
    return retDict

if __name__ == '__main__':
    app.run(debug=True, port=8000)