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
    #Thies two will be encrypted
    username = request.args.get('username')
    password = request.args.get('password')
    print(username, password)

    #dercypt password and username here

    #call login function here

    #This is how i want the return dict to look like
    #was the login successful? (was the username and password correct)
    #I alrealy have the username so i need to know if its an admin or not

    loginDict = {'login': True, 'isAdmin': True}
    return loginDict

@app.route('/createuser')
def createuser():
    fullname = request.args.get('fullname')
    username = request.args.get('username')
    password = request.args.get('password')
    print(username, password, fullname)
    #same shit here, decrypt password etc.
    #call the finction that creates the users in the database if they dont already exists
    #make sure the password and username is not empty

    createUserDict = {'creation': True}
    return createUserDict

@app.route('/history') #for regualr users and admin
def history():
    username = request.args.get('username')
    print(username)
    #Call function to get the history for the specific user
    historyDict = {"history": f"{username}:s history report"}
    return historyDict

@app.route('/userhistory') #only for admin
def userHistory():
    username = request.args.get('username')
    print(username)
    #Call function to get the history for ALL the users - Except the user that is making the call
    userHistoryDict = {'Agda': 'history report', 'Greta': 'history report', 'Janne': 'history report'}
    return userHistoryDict

if __name__ == '__main__':
    app.run(debug=True, port=8000)