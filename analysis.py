import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

## Navbar
from navbar import Navbar

nav = Navbar()

def Analysis(r,t, x):
    if r == 0:
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        print("tu o wiele lepiej bo r = ", r)

    else:
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        
    header = html.H3(
        '{}'. format(t)
    )

    graph = dcc.Graph(id='graph-with-slider')
    slider = dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )

    graph1 = dcc.Graph(id='gra')
    slider1 = dcc.RangeSlider(id = 'daty-slider',
            marks={i : {'label' : x[i], 'style':{'transform':'rotate(-45deg)', 'font-size':'15px'}} for i in range(0, len(x)) if i %2 ==1 },
            min = 1,
            max = len(x),
            value = [3, len(x)-2])

    layout = html.Div([
        nav,
        header,
        graph,
        slider,
        graph1,
        slider1

    ])
    return layout
    