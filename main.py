#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request

#Setting up Flask
app = Flask(__name__)

#This function brings the user to the login page.
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login Page')


# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)
