import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

from navbar import Navbar

nav = Navbar()

header = html.Div([html.H3(
        "Projects comparison"
    )], style={"margin-left":"5%"} )

params = [
    'NPV', 'IRR', 'Investment', 'Term',
    'Capacity', 'Power'
]

table = html.Div([
    dash_table.DataTable(
        id='table-edit',
        columns=(
            [{'id': 'Project', 'name': 'Project'}] +
            [{'id': p, 'name': p} for p in params]
        ),
        data=[
            dict(Project=i, **{param: 0 for param in params})
            for i in range(1, 5)
        ],
        style_header={ 'border': '2px solid black', 'fontWeight': 'bold', "textAlign" :"center", 'color': 'black' },
        editable=True,
        export_format='xlsx',
    ),
    html.Br(),
    dcc.Graph(id='table-output')
],  style={'width': "90%", "margin-left":"5%"})

def Table():
    layout = html.Div([
        nav,
        html.Br(),
        header,
        html.Br(),
        table
    ])
    return layout