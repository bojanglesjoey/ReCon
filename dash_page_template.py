import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('Go to Graphing Page', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Home Page', href='/page-1'),
])

#title of web page
app.title = 'ReCon'

page_2_layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='Climate Change Data Visualization', 
            className = "nine columns",
            style={'color' : 'white',
                'fontSize' : 50,
                'font-family' : 'Helvetica',
                'font-size' : 64,
                'background-image': 'url(https://raw.githubusercontent.com/bojanglesjoey/ReCon/master/banner.png)'}),
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
        dcc.Checklist(
            options=[
                {'label': 'Display Moving Average', 'value': 'MOVAVG'}
            ],
            values=['MOVAVG'],
            labelStyle={'display': 'inline-block'},
        )
    ], className = "row"),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(
                id='graph1',
            )
        ], className = "eight columns"),
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
            value=['CO2', 'H2O'],
            multi=False,
        ),
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
                {'label': 'Pressure', 'value': 'PRES'},
                {'label': 'Time', 'value': 'TIME'}
            ],
            value=['ALT', 'LAT', 'CONC', 'PRES', 'TIME'],
            multi=False,
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
                {'label': 'Pressure', 'value': 'PRES'},
                {'label': 'Time', 'value': 'TIME'}
            ],
            value=['ALT', 'LAT', 'CONC', 'PRES', 'TIME'],
            multi=False,
        ),
    ], className = "row"),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Home Page', href='/'),
])

page_1_layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='ReCon: Climate Change Research to Consumers', 
            className = "twelve columns",
            style={'color' : 'white',
                'fontSize' : 50,
                'font-family' : 'Helvetica',
                'font-size' : 64,
                'background-image': 'url(https://raw.githubusercontent.com/bojanglesjoey/ReCon/master/banner.png)'}),
    ], className = "row"),

    html.Div(children=[
        html.Img(
             src="https://fournews-assets-prod-s3b-ew1-aws-c4-pml.s3.amazonaws.com/media/2017/06/global-temperatures-nasa.jpg",
             className ="twelve columns",
             style={
                 'height': '100%',
                 'width': '100%',
                 'float': 'middle',
                 'position': 'relative',
                 'margin-top': 10,
             },
         ),
    ]),
    dcc.Textarea(
        value='Global temperatures are rising. This graph from Nasa shows changes in global temperatures over the years. The different lines show the data collected by separate research centres.',
        style={'width': '100%'}
    ),
    html.Div(children=[
        html.Img(
             src="https://fournews-assets-prod-s3-ew1-nmprod.s3.amazonaws.com/media/2017/06/co2-nasa.jpg",
             className ="twelve columns",
             style={
                 'height': '100%',
                 'width': '100%',
                 'float': 'middle',
                 'position': 'relative',
                 'margin-top': 10,
             },
         ),
    ]),
    dcc.Textarea(
        value='The amount of CO2 in the earth’s atmosphere is far higher than at any point in at least the last 400,000 years. And it’s still rising, this Nasa graph shows. CO2 levels have not been this high for at least three million years.',
        style={'width': '100%'}
    ),

    html.Div(children=[
        html.Img(
             src="https://fournews-assets-prod-s3-ew1-nmprod.s3.amazonaws.com/media/2017/06/carbon-emissions-global-final.png",
             className ="twelve columns",
             style={
                 'height': '100%',
                 'width': '100%',
                 'float': 'middle',
                 'position': 'relative',
                 'margin-top': 10,
             },
         ),
    ]),
    dcc.Textarea(
        value='Research by the International Energy Agency charts the amount of energy-related carbon dioxide emissions across the world. Emissions are starting to level off, thanks to increased use of renewable energy and improved technology.',
        style={'width': '100%'}
    ),

    html.Div(children=[
        html.Img(
             src="https://fournews-assets-prod-s3b-ew1-aws-c4-pml.s3.amazonaws.com/media/2017/06/arctic-sea-ice-minimum-nasa.png",
             className ="twelve columns",
             style={
                 'height': '100%',
                 'width': '100%',
                 'float': 'middle',
                 'position': 'relative',
                 'margin-top': 10,
             },
         ),
    ]),
    dcc.Textarea(
        value='Actic ice caps are melting. This shows the minimum amount of ice recorded in the Arctic each year. It is declining at a rate of 13.3 per cent every decade, according to Nasa.',
        style={'width': '100%'}
    ),

    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Graphing Page', href='/page-2'),
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_2_layout
    else:
        return page_1_layout 
    # You could also return a 404 "URL not found" page here

#callback for graph1
'''@app.callback(
    dash.dependencies.Output('graph1', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_graph(selector):
    data = []
    if 'SF' in selector:
        data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'})
    if 'MT' in selector:
        data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
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
    return figure'''

if __name__ == '__main__':
    app.run_server(debug=True)
