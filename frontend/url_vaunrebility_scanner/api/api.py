import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def fetchURLreport():
    #dir1 = {"valid": False}
    dir2 = {"valid": True, 1: "Website does not use HTTPS - HTTP is an unsecure protocol\n", 2: "URL was too long", 3: "too new website"}
    report = ""

    for i in range(1,3):
        if i == 3:
            report += dir2[i]
        else:
            report += dir2[i] + "\n"
    return report

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/scanner')
def scanner_start():
    return {'report': fetchURLreport()}
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)