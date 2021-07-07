import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Data download"),
                        html.P(
                            """
                         Please select file and drop in grey box below to download // .csv or .xlsx format //
                         """
                        ),
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        #html.H2("Graphic presentation"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "y": [10, 7, 9, 8, 11, 15, 17, 14, 12, 12, 7, 6, 10, 14], 'name': 'data-1'},
                                             {"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "y": [2, 5, 5, 5, 1, 1, -2, 7, 5, 2, 9, 9, 5, 6], 'type': 'bar', 'name': 'data-2'}],
                                    'layout': {'title': 'Dash Data Visualization Example'},
                                    },
                            style={
                                'borderWidth': '1px',
                                'borderStyle': 'solid',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                        ),
                    ],

                ),
            ]

        ), dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select File')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px',
                'background': "lightgrey"
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ],
    className="mt-4",
)


def Homepage():
    layout = html.Div([
        nav,
        body
    ])
    return layout


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.layout = Homepage()

if __name__ == "__main__":
    app.run_server()
