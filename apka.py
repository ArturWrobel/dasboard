import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go

from navbar import Navbar

nav = Navbar()

def body (x,z, text):
    
    return dbc.Container(
    [
       
               dbc.Col(
                  [
                     html.H1(text),                         
                   ],
                  
               ),
              dbc.Col(
                 [
                     dcc.Graph(
                         figure={"data": [{"x": x, "y": z}]}
                            ),
                        ]
                     ),
                

            dcc.Dropdown(id = 'drop',
    options=[
        {'label': 'costs', 'value': 'co'},
        {'label': 'sold', 'value': 'so'},
        {'label': 'result', 'value': 're'},
        {'label': 'cumulated', 'value': 'cu'}
    ],
    multi=True,
    value="re"
)  ,
html.Br(),
html.Br()
 ,
        html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'slider',
                                    #marks = {i : y[i] {‘label’ : available_dates_rangeslider[i], ‘style’:{‘transform’:‘rotate(-90deg)’, ‘font-size’:‘8px’}} for i in range(len(y))},
                                    marks={i : {'label' : x[i], 'style':{'transform':'rotate(-45deg)', 'font-size':'15px'}} for i in range(0, len(x)) if i %2 ==1 },
                                    min = 1,
                                    max = len(x),
                                    value = [3, len(x)-2])
                        ], style = {'width' : '100%',
                                    'fontSize' : '20px',
                                    'display': 'inline-block'}),
       ],
className="mt-4",
)


def Apka(x,z, text):
    layout = html.Div([
    nav,
    body(x,z, text)
    ])
    return layout



app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Apka([],[],'')