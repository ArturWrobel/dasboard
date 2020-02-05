import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

def body (x,z):
    return dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Heading"),
                     html.P(
                         """\
                        Don AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        AAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        AAAAAAAAAlis euismod.Donec sedodio dui."""
                                            ),
                           dbc.Button("View details", color="secondary"),
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
                     html.H2("Graph"),
                     dcc.Graph(
                         figure={"data": [{"x": x, "y": z}]}
                            ),
                        ]
                     ),
                ]
            ),

            dcc.Dropdown(
    options=[
        {'label': 'costs', 'value': 'co'},
        {'label': 'sold', 'value': 'so'},
        {'label': 'result', 'value': 're'},
        {'label': 'cumulated', 'value': 'cu'}
    ],
    value='MTL'
)  ,
html.Br(),
html.Br()
 ,
        html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'slider',
                                    #marks = {i : y[i] {‘label’ : available_dates_rangeslider[i], ‘style’:{‘transform’:‘rotate(-90deg)’, ‘font-size’:‘8px’}} for i in range(len(y))},
                                    marks={i : {'label' : x[i], 'style':{'transform':'rotate(-90deg)', 'font-size':'15px'}} for i in range(0, len(x)) if i %2 ==0},
                                    min = 1,
                                    max = len(x),
                                    value = [1, len(x)-2])
                        ], style = {'width' : '100%',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
       ],
className="mt-4",
)

def Apka(x,z):
    layout = html.Div([
    nav,
    body(x,z)
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Apka([],[])

if __name__ == "__main__":
    app.run_server()