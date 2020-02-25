import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from navbar import Navbar

nav = Navbar()

def Apka(r, t, df1):
    if r == 0:
        print ("załadowane!")
        ti = pd.to_datetime(df1.data)
        ti = ti.dt.date
    else:
        print ("nie załadowane")
        ti =[]
        
        
    header = html.H3(
        ['{}'. format(t)], style={"color": "red"}
    )

    graph = dcc.Graph(id='gra')
    slider = dcc.RangeSlider(id = 'daty-slider',
            marks={i : {'label' : ti[i], 'style':{'font-size':'15px'}} for i in range(0, len(ti)) if i %2 == 1 },
            min = 0,
            max = len(ti)-1,
            value = [0, len(ti)])

    drop = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC',
        multi=True
    ),
    html.Div(id='dd-output-container')
])

    layout = html.Div([
        nav,
        header,
        graph,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        slider,
        html.Br(),
        html.Br(),
        drop
    ])
    return layout
    