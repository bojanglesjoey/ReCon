from flask import Flask, render_template, request
from datetime import datetime
import dash_app

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def analysis():
	dash = dash_app.add_dash(__name__, app)

if __name__ == '__main__':
    app.run(debug=True)

