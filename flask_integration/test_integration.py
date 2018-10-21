from flask import Flask
import Dash_Plot
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/start')
def start():
	return "start"

@app.route('/dash')
def dash():
	return Dash_Plot.create_app(app)

if __name__ == '__main__':
    app.run()