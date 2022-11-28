from flask import Flask, request
import time
import main as main
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/scanner')
def scanner():
    sTime = time.time()
    retDict = main.main(request.args.get('url'))
    if retDict["valid"] == "True":
        retDict["exeTime"] = f'\n\nThe scan took {(time.time() - sTime):.2f} seconds'
    return retDict

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username, password)

    #1. call function that authenticates the user (username, password)

    #2. call function that checks if that user is an admin

    dict = {'login': True, 'isAdmin': True, 'userToken': 'random hash value'}
    return dict

@app.route('/createuser')
def createuser():
    new_username = request.args.get('username')
    new_fullname = request.args.get('fullname')
    new_password = request.args.get('password')
    new_token = request.args.get('newToken')

    #to authenticate the user that is trying to create the user
    username = request.args.get('user')
    user_token = request.args.get('user_token')

    print('VALS:',new_username, new_fullname, new_password, new_token,'\nUser,token combo:', username, user_token)

    #1. call function that authenticates the user (username, user_token)

    #2. call function that checks if that user is an admin

    #3. call function that checks if the username is available

    #4. create the new user in the database if all above is true

    dict = {'creation': True, 'auth': True}
    return dict

@app.route('/history')
def history():
    username = request.args.get('username')
    user_token = request.args.get('user_token')
    print(username, user_token)

    #1. call function that authenticates the user (username, user_token)

    #2. call function that returns the history dict

    dict = {"history": f"{username}:s history report", "auth": True}
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