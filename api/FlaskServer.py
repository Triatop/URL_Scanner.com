from flask import Flask, request
import time
import main as main
from flask_cors import CORS
from DB_Controller import DBController
from UrlController import UrlController
from datetime import date
from ReportMaker import ReportMaker


app = Flask(__name__)
CORS(app)


@app.route('/scanner')
def scanner():
    sTime = time.time()
    username = request.args.get('username')
    user_token = request.args.get('user_token')

    db_obj = DBController()

    #Validate user so the scan does not get stored on with the wrong user id
    if( not db_obj.validateUser(username, user_token) and username != ""):
        return {'report': 'Error: Authentication invalid'}
    

    retDict = main.main(request.args.get('url'), username)
    if retDict["valid"] == True:
        retDict["exeTime"] = f'\n\nScan time: {(time.time() - sTime):.2f} s'
    return retDict

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    db_obj = DBController()

    if(not db_obj.loginUser(username, password)):
        return {'login': False}

    return {'login': True, 'isAdmin': db_obj.authenticateAdmin(username), 'userToken': db_obj.getUserToken(username)}

@app.route('/createuser')
def createuser():
    new_username = request.args.get('username')
    new_fullname = request.args.get('fullname')
    new_password = request.args.get('password')
    new_token = request.args.get('newToken')
    new_adminPriv = request.args.get('adminPriv', type=lambda v: v == 'true')

    #to authenticate the logged in user that is trying to create the user
    username = request.args.get('user')
    user_token = request.args.get('user_token')

    db_obj = DBController()

    #1. call function that authenticates the user (username, user_token)
    if(not db_obj.validateUser(username, user_token)):
        return {'response': 'ERROR: Authentication Invalid!'}

    #2. call function that checks if that user is an admin
    if(not db_obj.authenticateAdmin(username)):
        return {'response': 'ERROR: Authentication Invalid!'}

    #3. input string handeling
    if(len(new_username)<5):
        return{'response':'Username must be atleast 5 characters long'}
    if(len(new_password)<4):
        return{'response':'Password must be atleast 4 characters long'}
    if(len(new_username) > 50 or len(new_password) > 100 or len(new_fullname) > 50):
        return{'response':'Input exceeded limit'}
    
    #4. call function that checks if the username is available
    if(db_obj.checkUsernameExists(new_username)):
        return {'response': f'The username {new_username} was already taken'}

    #4. create the new user in the database if all above is true
    db_obj.createUser(new_username, new_password, new_fullname, new_token, new_adminPriv)
    return {'response': f'The user {new_username} was created'}

@app.route('/history')
def history():
    username = request.args.get('username')
    user_token = request.args.get('user_token')

    db_obj = DBController()
    u_ctrl = UrlController()
    rmaker = ReportMaker()

    #1. call function that authenticates the user (username, user_token)
    if(not db_obj.validateUser(username, user_token)):
        return {'auth': False}

    #2. call function that returns the history dict
    history = db_obj.getHistory(username)

    #3. Format history dict
    histDict = {}
    for index, value in enumerate(history):
        a_dict = {int(k):v for k,v in value[3].items()} # convert keys to integers as to jsaonb converts keys to strings.
        rmaker.createReport(a_dict, value[4], value[5])
        histDict[index] = {'url': u_ctrl.decryptUrl(value[0]), 'date': str(value[1]), 'safe': value[2], 'report': rmaker.getReport()}

    dict = {"auth": True, "history": histDict}
    return dict

@app.route('/userhistory') #only for admin
def userHistory():
    username = request.args.get('username')
    user_token = request.args.get('user_token')

    db_obj = DBController()
    u_ctrl = UrlController()
    rmaker = ReportMaker()

    #1. call function that authenticates the user (user, user_token)
    if(not db_obj.validateUser(username, user_token)):
        return {'auth': False}
    #2. call function that checks if that user is an admin
    if(not db_obj.authenticateAdmin(username)):
        return {'auth': False}

    #3. call function to get the history for ALL the users - Except the user that is making the call
    allUserHistDict = {}
    for name in db_obj.getAllUsernames():
        histDict = {}
        for index, value in enumerate(db_obj.getHistory(name)):
            a_dict = {int(k):v for k,v in value[3].items()} # convert keys to integers as to jsaonb converts keys to strings.
            rmaker.createReport(a_dict, value[4], value[5])
            histDict[index] = {'url': u_ctrl.decryptUrl(value[0]), 'date': str(value[1]), 'safe': value[2], 'report': rmaker.getReport()}
        allUserHistDict[name] = histDict

    return {'auth': True, 'userhistory': allUserHistDict}

if __name__ == '__main__':
    app.run(debug=True, port=8000)