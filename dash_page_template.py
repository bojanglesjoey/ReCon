import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

#title of web page
app.title = 'Dash Page'

app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='Climate Change Data Visualization', 
            className = "nine columns"),
        html.Img(
            src="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Csa-asc_logo.svg/1200px-Csa-asc_logo.svg.png",
            className ="two columns",
            style={
                'height': '15%',
                'width': '15%',
                'float': 'right',
                'position': 'relative',
                'margin-top': 10,
            },
        ),
    ], className = "row"),

    html.Div(children=[
        html.Div(children='''
            Choose a gas of interest.
        '''),

        dcc.Dropdown(
            id='dropdown1',
            options=[
                {'label': 'Carbon Dioxide', 'value': 'CO2'},
                {'label': 'Water Vapour', 'value': 'H2O'}
            ],
            #default value(s)
            #value=['MTL', 'NYC'],
            multi=False
        ),
    ], className = "row"),
    

    html.Div(children=[
        dcc.Graph(
            id='graph1',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'xaxis' : dict(
                        title='x Axis',
                        titlefont=dict(
                        family='Courier New, monospace',
                        size=20,
                        color='#7f7f7f'
                    )),
                    'yaxis' : dict(
                        title='y Axis',
                        titlefont=dict(
                        family='Helvetica, monospace',
                        size=20,
                        color='#7f7f7f'
                    ))
                }
            }
        )
    ], className = "row"),

    html.Div(children=[
        html.Div(children='''
            Select an x-axis metric.
        '''),

        dcc.Dropdown(
            id='dropdown2',
            options=[
                {'label': 'Altitude', 'value': 'ALT'},
                {'label': 'Latitude', 'value': 'LAT'},
                {'label': 'Gas Concentration', 'value': 'CONC'},
                {'label': 'Pressure', 'value': 'PRES'}
            ],
            multi=False
        ),
    ], className = "row"),

    html.Div(children=[
        html.Div(children='''
            Select a y-axis metric.
        '''),

        dcc.Dropdown(
            id='dropdown3',
            options=[
                {'label': 'Altitude', 'value': 'ALT'},
                {'label': 'Latitude', 'value': 'LAT'},
                {'label': 'Gas Concentration', 'value': 'CONC'},
                {'label': 'Pressure', 'value': 'PRES'}
            ],
            multi=False
        ),
    ], className = "row")
])

if __name__ == '__main__':
    app.run_server(debug=True)