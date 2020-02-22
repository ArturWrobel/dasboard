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
)],
className="mt-4",
)


def Apka(x,z, text):
    layout = html.Div([
    nav,
    body(x, z, text)
    ])
    return layout



app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Apka([],[],'')