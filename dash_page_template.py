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

arguments = [-1,-1,-1,-1,-1]
#title of web page
app.title = 'ReCon'

page_2_layout = html.Div([
    html.Div([
        html.Div([
            html.H1(children='Climate Change Data Visualization', 
                className = "twelve columns",
                 style={'color' : 'white',
                'fontSize' : 50,
                'font-family' : 'Helvetica',
                'font-size' : 64,
                'background-image': 'url(https://raw.githubusercontent.com/bojanglesjoey/ReCon/master/banner.png)'}),
        ], className = "row"),

        html.Div([
            dcc.Checklist(
                id='checklist1',
                options=[
                    {'label': 'Display Moving Average', 'value': 'MOVAVG'}
                ],
                #note: use "values" property for checklists
                values=['MOVAVG'],
                labelStyle={'display': 'inline-block'},
            )
        ], className = "row"),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph1',
                )
            ], className = "eight columns"),
        ], className = "row"),

        html.Div([
            html.Div([
                html.Div('''
                    Choose a gas of interest:
                '''),

                dcc.Dropdown(
                    id='dropdown1',
                    options=[
                        {'label':'C2H2','value':'C2H2'},
                        {'label':'CO2','value':'CO2'},
                        {'label':'HNO3','value':'HNO3'},
                        {'label':'C2H6','value':'C2H6'},
                        {'label':'COCl2','value':'COCl2'},
                        {'label':'HNO4','value':'HNO4'},
                        {'label':'CCl2F2','value':'CCl2F2'},
                        {'label':'COClF','value':'COClF'},
                        {'label':'N2','value':'N2'},
                        {'label':'CCl3F','value':'CCl3F'},
                        {'label':'COF2','value':'COF2'},
                        {'label':'N2O5','value':'N2O5'},
                        {'label':'CCl4','value':'CCl4'},
                        {'label':'CO','value':'CO'},
                        {'label':'N2O','value':'N2O'},
                        {'label':'CF4','value':'CF4'},
                        {'label':'H2CO','value':'H2CO'},
                        {'label':'NO2','value':'NO2'},
                        {'label':'CFC113','value':'CFC113'},
                        {'label':'H2O2','value':'H2O2'},
                        {'label':'NO','value':'NO'},
                        {'label':'CH3Cl','value':'CH3Cl'},
                        {'label':'H2O','value':'H2O'},
                        {'label':'O2','value':'O2'},
                        {'label':'CH3OH','value':'CH3OH'},
                        {'label':'HCl','value':'HCl'},
                        {'label':'O3','value':'O3'},
                        {'label':'CH4','value':'CH4'},
                        {'label':'HCN','value':'HCN'},
                        {'label':'OCS','value':'OCS'},
                        {'label':'CHF2Cl','value':'CHF2Cl'},
                        {'label':'HCOOH','value':'HCOOH'},
                        {'label':'ClONO2','value':'ClONO2'},
                        {'label':'HF','value':'HF'}
                    ],
                    value=["C2H2","CO2","HNO3","C2H6","COCl2","HNO4","CCl2F2","COClF","N2","CCl3F","COF2","N2O5","CCl4","CO","N2O","CF4","H2CO","NO2","CFC113","H2O2","NO","CH3Cl","H2O","O2","CH3OH","HCl","O3","CH4","HCN","OCS","CHF2Cl","HCOOH","ClONO2","HF"],
                    #multi=False,
                ),
            ], className = "six columns"),

            html.Div([
                html.Div('''
                    Choose a type of graph:
                '''),

                dcc.Dropdown(
                    id='dropdown2',
                    options=[
                        {'label':'3D Scatter Plot','value':'Scatter3d'},
                        {'label':'2D Scatter Plot','value':'Scatter'},
                        {'label':'Surface Plot','value':'Surface'},
                        {'label':'Heat Map','value':'Heatmap'}
                    ],
                    value=['SCAT','SURF','HEAT'],
                    #multi=False,
                ),
            ], className = "six columns"),
        ], className = "row"),

        html.Div([
            html.Div('''
                Select an x-axis metric:
            '''),

            dcc.Dropdown(
                id='dropdown3',
                options=[
                    {'label': 'Altitude', 'value': 'altitude'},
                    {'label': 'Latitude', 'value': 'latitude'},
                    {'label': 'Longitude', 'value': 'longitude'},
                    {'label': 'Beta Angle', 'value': 'beta_angle'},
                    {'label': 'Hour', 'value': 'hour'},
                    {'label': 'Day', 'value': 'day'},
                    {'label': 'Month', 'value': 'month'},
                    {'label': 'Year', 'value': 'year'},
                ],
                value=['altitude','latitude','longitude','beta_angle','hour','day','month','year'],
                #multi=False,
            ),
        ], className = "row"),

        html.Div([
            html.Div('''
                Select a y-axis metric:
            '''),

            dcc.Dropdown(
                id='dropdown4',
                options=[
                    {'label': 'Altitude', 'value': 'altitude'},
                    {'label': 'Latitude', 'value': 'latitude'},
                    {'label': 'Longitude', 'value': 'longitude'},
                    {'label': 'Beta Angle', 'value': 'beta_angle'},
                    {'label': 'Hour', 'value': 'hour'},
                    {'label': 'Day', 'value': 'day'},
                    {'label': 'Month', 'value': 'month'},
                    {'label': 'Year', 'value': 'year'},
                    {'label': 'Temperature', 'value': 'temperature'},
                    {'label': 'Temperature Fit', 'value': 'temperature_fit'},
                    {'label': 'Pressure', 'value': 'pressure'},
                    {'label': 'Concentration', 'value': 'concentration'},
                ],
                value=['altitude','latitude','longitude','beta_angle','hour','day','month','year','temperature','temperature_fit','pressure','concentration'],
                #multi=False,
            ),
        ], className = "row"),

        html.Div([
            html.Div('''
                Select a z-axis metric:
            '''),

            dcc.Dropdown(
                id='dropdown5',
                options=[
                    {'label': 'Altitude', 'value': 'altitude'},
                    {'label': 'Latitude', 'value': 'latitude'},
                    {'label': 'Longitude', 'value': 'longitude'},
                    {'label': 'Beta Angle', 'value': 'beta_angle'},
                    {'label': 'Hour', 'value': 'hour'},
                    {'label': 'Day', 'value': 'day'},
                    {'label': 'Month', 'value': 'month'},
                    {'label': 'Year', 'value': 'year'},
                    {'label': 'Temperature', 'value': 'temperature'},
                    {'label': 'Temperature Fit', 'value': 'temperature_fit'},
                    {'label': 'Pressure', 'value': 'pressure'},
                    {'label': 'Concentration', 'value': 'concentration'},
                ],
                value=['altitude','latitude','longitude','beta_angle','hour','day','month','year','temperature','temperature_fit','pressure','concentration'],
                #multi=False,
            ),
        ], className = "row"),
            html.Br(),
    dcc.ConfirmDialogProvider(
        children=html.Button(
             'Publish',
        ),
        id='button-publish',
        message='Publishing your findings will be implemented in the future!'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Home Page', href='/'),
    ]),
    html.Div(id='gas_type'),
    html.Div(id='graph_type'),
    html.Div(id='x-axis'),
    html.Div(id='y-axis'),
    html.Div(id='z-axis'),
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
                 'height': '75%',
                 'width': '75%',
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
                 'fontSize' : 20,
                 'font-family' : 'Helvetica',
                 'height': '75%',
                 'width': '75%',
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
                 'fontSize' : 20,
                 'font-family' : 'Helvetica',
                 'height': '75%',
                 'width': '75%',
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
                 'fontSize' : 20,
                 'font-family' : 'Helvetica',
                 'height': '75%',
                 'width': '75%',
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

@app.callback(
    dash.dependencies.Output('graph1', 'figure'),
    [dash.dependencies.Input('dropdown1', 'value')])
def select_gas_data(selector):
    data = []
    if type(selector) == str:
        if 'CO2' in selector:
            data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'CO2'})
        if 'H2O' in selector:
            data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'H2O'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Data Visualization',
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
    return figure

@app.callback(
    dash.dependencies.Output('gas_type', 'children'),
    [dash.dependencies.Input('dropdown1', 'value')]
)
def update_gas_type(gas_type):
    #print(gas_type)
    arguments[0] = gas_type

@app.callback(
    dash.dependencies.Output('graph_type', 'children'),
    [dash.dependencies.Input('dropdown2', 'value')]
)
def update_graph_type(graph_type):
    #print(graph_type)
    arguments[1] = graph_type

@app.callback(
    dash.dependencies.Output('x-axis', 'children'),
    [dash.dependencies.Input('dropdown3', 'value')]
)
def update_x_axis(x_axis):
    #print(x_axis)
    arguments[2] = x_axis

@app.callback(
    dash.dependencies.Output('y-axis', 'children'),
    [dash.dependencies.Input('dropdown4', 'value')]
)
def update_y_axis(y_axis):
    #print(y_axis)
    arguments[3] = y_axis

@app.callback(
    dash.dependencies.Output('z-axis', 'children'),
    [dash.dependencies.Input('dropdown5', 'value')]
)
def update_z_axis(z_axis):
    #print(z_axis)
    arguments[4] = z_axis


if __name__ == '__main__':
    app.run_server(debug=True)
