from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
	"""
	This is the main pae of the site
	"""
	return 'Hello'

@app.route('/v1/getinputs')
def get_inputs():
	pass

def generate_sugesstions():
	pass
	
