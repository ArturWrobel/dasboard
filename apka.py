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
        ti = pd.to_datetime(df1.data)
        ti = ti.dt.date
    else:
        ti =[]
        
        
    header = html.H3(
        ['{}'. format(t)], style={"color": "red"}
    )

    graphi = dcc.Graph(id='apka')
    sliderr = dcc.RangeSlider(id = 'multi-slider',
            marks={i : {'label' : ti[i], 'style':{'font-size':'15px'}} for i in range(0, len(ti)) if i %2 == 1 },
            min = 0,
            max = len(ti)-1,
            value = [0, len(ti)])

    a = "Average Costs during Feb: 4'091,1."
    b = "Highest Sold proceeds for Feb: 10'000."
    c = "Lowest result during Feb: -2'000."
    d = "Highest cumulated result in Feb: 17'500."


    drop = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Costs', 'value': a},
            {'label': 'Sold', 'value': b},
            {'label': 'Result', 'value': c},
            {'label': 'Cumulated', 'value': d},
        ],
        multi=False
    ),
    html.Br(),
    html.Div(id='dd-output-container')
])

    layout = html.Div([
        nav,
        header,
        graphi,
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        sliderr,
        html.Br(),
        html.Br(),
        drop
    ])
    return layout
    