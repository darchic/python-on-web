from flask import Flask, session
from cheker import check_logged_in

app=Flask(__name__)
app.secret_key='YouWillNeverGuess'
@app.route('/')
def hello()->str:
    return 'Hello from the simple webapp'
@app.route('/page1')
@check_logged_in
def page1()->str:
    return 'This is page1'
@app.route('/page2')
@check_logged_in
def page2()->str:
    return 'This is page2'

@app.route('/login')
def do_loggin()->str:
    session['logged_in']=True
    return 'You are logged in'

@app.route('/logout')
def do_logout()->str:
    session.pop('logged_in')
    return 'You are logged out'
if __name__=='__main__':
    app.run(debug=True)