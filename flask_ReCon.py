from flask import Flask, render_template, url_for

server = Flask(__name__)

posts = [
	{
		'author': 'Researcher 1',
		'title': 'CO2 Changes',
		'content': 'Concentration of CO2 over the last 10 years',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Researcher 2',
		'title': 'Rising HCFC',
		'content': 'Increasing amounts of HCFC in our atmosphere',
		'date_posted': 'May 1, 2018'
	}
]
#"/" root
@server.route("/")
@server.route("/home")
def hello():
    return render_template('home.html',posts=posts,title='Home Page')

@server.route("/about")
def about():
	return render_template('about.html',title='About Page')

#only true if running script directly
if __name__ == '__main__':
	server.run(debug=True)