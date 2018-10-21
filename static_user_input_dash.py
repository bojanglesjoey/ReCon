import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

dash_app = dash.Dash(__name__)

dash_app.layout = html.Div(children=[
	html.H1('Data Visualization'),
	##Input from dash_core_components, not from dash.dependencies
	dcc.Input(id='input', value='Enter something', type='text'),
	html.Div(id='output')
	])

@dash_app.callback(
	Output(component_id='output', component_property='children'),
	[Input(component_id='input', component_property='value')])
def update_value(input_data):
	try: 
		return "Input: {}".format(input_data)
	except:
		return "Error"

#only true if running script directly
if __name__ == '__main__':
	dash_app.run_server(debug=True)