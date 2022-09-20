import URL_Object as urlObject
import UrlController as urlCtr
from flask import Flask, request



app = Flask(__name__)


@app.route('/backendAPI')
def members():
    return main()

def main():
    ctr = urlCtr.UrlController()
    valid = ctr.validateUrl(request.args.get('url'))
    if not valid:
        return {'valid': valid}
    #Continue
    return 'Lesgooo'


if __name__ == '__main__':
    app.run(debug=True, port=5000)