
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import json
from dataset_itpr import FormatNC


#x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 200).transpose()
data = FormatNC()

def make_graph(graph_type,layout):
	#return the layout, app.layout should be set to this.
	#args: graph type, go.graph function object
	layout = html.Div([
		dcc.Graph(
			figure=go.Figure(
			data=[
				graph_type()
			],
			layout=layout()
		),
		style={'height': 300},
		id='my-graph'
	),
		html.Div(id='output')
	])
	return layout

def display_hoverdata(hoverData, clickData):
	return [
		json.dumps(hoverData, indent=2),
		html.Br(),
		json.dumps(clickData, indent=2)
	]

def Surface_lag(gas,x_name,y_name,z_name):
	#lag - layout and graph
	x,y,z = data._read_nc_files(gas,x_name ,y_name ,z_name)
	graph = lambda: go.Surface(x=x, y=y, z=z)
	layout = lambda: go.Layout(
			title='%s Emissions, %s vs %s and %s'%(gas,z_name,x_name,y_name),
			showlegend=True,
			scene = dict(
			xaxis = dict(title = x_name),
			yaxis = dict(title = y_name),
			zaxis = dict(title = z_name)),
			legend=go.layout.Legend(
				x=0,
				y=1.0
			),
			margin=go.layout.Margin(l=100, r=0, t=0, b=0)
		)
	return graph, layout

def Scatter3d_lag(gas,x_name,y_name,z_name):
	x,y,z = data._read_nc_files(gas,x_name ,y_name ,z_name)
	graph = lambda: go.Scatter3d(
				x=x,
				y=y,
				z=z,
				mode='markers',
				marker=dict(
					size=12,
					color=z,   
					colorscale='Viridis', 
					opacity=0.8
				))
	layout = lambda: go.Layout(
			title='%s Emissions, %s vs %s and %s'%(gas,z_name,x_name,y_name),
			scene = dict(
			xaxis = dict(title = x_name),
			yaxis = dict(title = y_name),
			zaxis = dict(title = z_name)),
			margin=go.layout.Margin(l=100, r=0, t=0, b=0)
		)

	return graph, layout

def Scatter_lag(gas,x_name,y_name):
	x,y = data._read_nc_files(gas,x_name ,y_name)
	graph = lambda: go.Scatter(
					x=x,
					y=y,
					mode='markers',
					opacity=0.7,
					marker={
						'size': 5,
						'line': {'width': 0.5, 'color': 'white'}
					}
				)

	layout = lambda: go.Layout(
				xaxis = dict(title = x_name),
				yaxis = dict(title = y_name),
				margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
				hovermode='closest'
			)

	return graph, layout

def Heatmap_lag(gas,x_name,y_name,z_name):
	x,y,z = data._read_nc_files(gas,x_name ,y_name,z_name)
	graph = lambda: go.Heatmap(
					x=x,
					y=y,
					z=z,
					colorscale='Viridis',
				)

	layout = lambda: go.Layout(
				scene = dict(
				xaxis = dict(title = x_name),
				yaxis = dict(title = y_name),
				zaxis = dict(title = z_name)),
				margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
			)

	return graph, layout


def get_graph(graph, *args):
	#args: gas,x,y,z
	graphs = {key[:-4]:value for key, value in globals().items() if "_lag" in key}
	graph, layout = graphs[graph](*args)
	return make_graph(graph, layout)


if __name__ == '__main__':
	x_name = 'altitude' 
	z_name = 'concentration' 
	y_name = 'beta_angle' 
	gas = "CFC113"
	app.layout = get_graph("Heatmap",gas,x_name,y_name,z_name)
	app.run_server()

"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import testing.get_data as gd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

x,y = gd.get_random_data()

app.layout = html.Div([
	dcc.Graph(
		id='life-exp-vs-gdp',
		figure={
			'data': [
				go.Scatter(
					x=x,
					y=y,
					mode='markers',
					opacity=0.7,
					marker={
						'size': 5,
						'line': {'width': 0.5, 'color': 'white'}
					},
					name="asdf"
				)
			],
			'layout': go.Layout(
				xaxis={'type': 'log', 'title': 'GDP Per Capita'},
				yaxis={'title': 'Life Expectancy'},
				margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
				legend={'x': 0, 'y': 1},
				hovermode='closest'
			)
		}
	)
])


if __name__ == '__main__':
	app.run_server()



"""