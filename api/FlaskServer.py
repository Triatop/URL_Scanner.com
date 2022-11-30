from flask import Flask, request
import time
import main as main
from flask_cors import CORS
from DB_Controller import DBController
from datetime import date


app = Flask(__name__)
CORS(app)


@app.route('/scanner')
def scanner():
    sTime = time.time()
    retDict = main.main(request.args.get('url'),request.args.get('username'))
    if retDict["valid"] == "True":
        retDict["exeTime"] = f'\n\nThe scan took {(time.time() - sTime):.2f} seconds'
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

    #to authenticate the user that is trying to create the user
    username = request.args.get('user')
    user_token = request.args.get('user_token')

    db_obj = DBController()

    #1. call function that authenticates the user (username, user_token)
    if(not db_obj.validateUser(username, user_token)):
        return {'creation': False, 'auth': False}

    #2. call function that checks if that user is an admin
    if(not db_obj.authenticateAdmin(username)):
        return {'creation': False, 'auth': False}

    #3. call function that checks if the username is available
    if(db_obj.checkUsernameExists(new_username)):
        return {'creation': False, 'auth': True}

    #4. create the new user in the database if all above is true
    db_obj.createUser(new_username, new_password, new_fullname, new_token, new_adminPriv)

    dict = {'creation': True, 'auth': True}
    return dict

@app.route('/history')
def history():
    username = request.args.get('username')
    user_token = request.args.get('user_token')

    db_obj = DBController()
    #1. call function that authenticates the user (username, user_token)
    if(not db_obj.validateUser(username, user_token)):
        return {'auth': False}

    #2. call function that returns the history dict
    history = db_obj.getHistory(username)
    histDict = ''
    for index, value in enumerate(history):
        histDict += str(index + 1)+ ': \tURL: ' + value[0]+ ' \t\tDATE: ' + str(value[1]) + ' \t\tSAFE: ' + str(value[2]) + '\n'

    dict = {"history": histDict, "auth": True}
    return dict

@app.route('/userhistory') #only for admin
def userHistory():
    username = request.args.get('username')
    user_token = request.args.get('user_token')
    print(username, user_token)

    #1. call function that authenticates the user (user, user_token)

    #2. call function that checks if that user is an admin

    #3. call function to get the history for ALL the users - Except the user that is making the call
    hist_dict = {'Agda': 'history report', 'Greta': 'history report', 'Janne': 'history report'}
    dict = {'auth': True, 'history': hist_dict}
    return dict

if __name__ == '__main__':
    app.run(debug=True, port=8000)