import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

## Navbar
from navbar import Navbar

nav = Navbar()

def Charts(r,t, x, df1):
    if r == 0:
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        print ("załadowane!")
        print (df1["data"][0])
        ti = pd.to_datetime(df1.data)
        ti = ti.dt.date
        print("data", ti[0])
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        print ("nie załadowane")
        ti =[]
        
        
    header = html.H3(
        '{}'. format(t)
    )

    graph1 = dcc.Graph(id='graph-with-slider')
    slider1 = dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )

    graph = dcc.Graph(id='gra')
    slider = dcc.RangeSlider(id = 'daty-slider',
            marks={i : {'label' : ti[i], 'style':{'font-size':'15px'}} for i in range(0, len(ti)) if i %2 == 1 },
            min = 0,
            max = len(ti)-1,
            value = [0, len(ti)])

    layout = html.Div([
        nav,
        header,
        graph,
        html.Br(),
        html.Br(),
        slider

    ])
    return layout
    