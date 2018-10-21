
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import json
x = 5
y = 10
app = dash.Dash()


def make_graph(graph_type):
    #return the layout, app.layout should be set to this.
    #args: graph type, go.graph function object
    layout = html.Div([
        dcc.Graph(
            figure=go.Figure(
            data=[
                graph_type(
                    x=[0,1,2,3,4],
                    y=np.arange(y),
                    z=np.arange(x*y).reshape(x,y)
                )
            ],
            layout=go.Layout(
                title='US Export of Plastic Scrap',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )
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


if __name__ == '__main__':
    app.layout= make_graph(go.Heatmap)
    app.run_server(debug=True)

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