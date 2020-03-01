import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from navbar import Navbar

nav = Navbar()

def Calc(r, t, df1):
    if r == 0:
        ti = pd.to_datetime(df1.data)
        ti = ti.dt.date
        desc = df1.describe()
    else:
        ti =[]
        desc = ""
        
    header = html.H3(
        ['{}'. format(t)], style={"color": "red"}
    )

    comment = html.H3(
        ['{}'. format(desc)], style={"color": "red"}
    )

    layout = html.Div([
        nav,
        header,
        html.Br(),
        html.Br(),
        comment

    ])
    return layout
    