from flask import Flask, session
app = Flask(__name__)
# The secret key is needed to sign the session cookie
app.config['SECRET_KEY'] = 'randomstring'

@app.route('/login/<name>')
def login(name):
	session['username'] = name
	return 'Added {} to session'.format(name)

@app.route('/account')
def account():
	return 'Hello {}'.format(session['username'])