from dash import dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html

def add_dash(name, server):
	app = dash.Dash(name, server=server)
	app.layout = html.Div(children=[
	html.H1('Test'),
	#dcc: dash core components 
	#required for dash graphs
	dcc.Graph(id='example',
				figure={
					'data': [
						{'x':[1,2,3,4,5], 'y':[5,6,7,8,9], 'type':'line', 'name':'boats'},
						{'x':[7,6,5,4,3], 'y':[12,11,10,9,8], 'type':'bar', 'name':'cars'},
						],
					'layout': {
						'title':'Basic Dash Example'
					}
				})
	])

	return app.server