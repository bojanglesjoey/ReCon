import dash
import dash_core_components as dcc
import dash_html_components as html
import flask_integration.Dash_Plot as dp
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

arguments = [-1,-1,-1,-1,-1]

#title of web page
app.title = 'Dash Page'

app.layout = html.Div([
    html.Div([
        html.Div([
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
            ], className = "twelve columns"),
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
    ]),
    html.Div(id='gas_type'),
    html.Div(id='graph_type'),
    html.Div(id='x-axis'),
    html.Div(id='y-axis'),
    html.Div(id='z-axis'),
])

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

@app.callback(
   dash.dependencies.Output('graph1', 'figure'),
   [dash.dependencies.Input('dropdown5', 'value')])
def select_gas_data(selector):
    x_name = 'altitude' 
    z_name = 'concentration' 
    y_name = 'beta_angle' 
    gas = "CFC113"
    return dp.get_graph("Heatmap",gas,x_name,y_name,z_name)


if __name__ == '__main__':
    app.run_server(debug=True)

