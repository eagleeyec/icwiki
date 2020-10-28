# Flask

## Hello world

	from flask import Flask

	api = Flask(__name__)

	@api.route('/')
	def index():
		return 'Hello world'

## Route examples

	# Route with optional param
	@app.route('/', defaults={'name': 'Dave'})
	@app.route('/name<string:name>')

	# Use POST or other methods
	@app.route('/', methods=['POST'])

## Query params

	from flask import Flask, request

	app = Flask(__name__)

	@app.route('/')
	def query():
		name = request.args.get('name')

## Json input data

Use this if you are passing json into the endpoint

	@app.route('/')
	def jsoninput():
		data = request.get_json()

## Respond to method

You can also do this as 2 sperate route definitions with different methods

	@app.route('/someform', methods=['GET', 'POST'])
	def someform():
		if request.method == 'POST':
			return 'Processed the form'
		else:
			return '<form>...</form>'

## Redirect user

	import url_for, redirect

	@app.route('/login')
	def login():
		# Confirm login ...
		return redirect(url_for('accountpage', param1='value1'))