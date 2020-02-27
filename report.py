import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import datetime

from fpdf import FPDF
from reportlab.pdfgen import canvas
from PIL import Image

from navbar import Navbar

nav = Navbar()

def pdf_rep():
    today = datetime.date.today()

    c = canvas.Canvas("test.pdf")
    im = Image.open("orange.jpg")
    c.drawInlineImage(im, 280, 780, width = 50, height = 50)
    c.drawString(280,750,"Raport")
    c.drawString(500,750, "{}".format(today))
    gr = Image.open("newplot.png")
    c.drawString(70,710, "Chart presents sales evolution during February.")
    c.drawInlineImage(gr, 150, 420, width = 300, height = 250)
    c.drawString(70,340, "Please feel free to contact us for further details.")
    c.drawString(370,300, "Regards")
    c.drawString(370,270, "Finance team")
    c.save()

def Report(r, t, df1):
    if r == 0:
        t = ""
        x=[1,2,3,4,5,6,7,8,9]
        y=[8,1,7,4,5,3,1,6,8]\
        
        a=[1,2,3,4,5,6,7,8,9]
        b=[18,15,3,14,1,13,11,6,18]
        text = "Average daily turnover during current month: 55.5 item" + "This is report regarding latest sales evolution. Current developments precent compeling trends but we have to spure marketing and improve logistics of sold items."
    else:
        ti =[]
        x=[]
        y=[]
        a=[]
        b=[]
        text = ""
        
    header = html.H3(['{}'. format(t)], style={"color": "red"}
        
    )

    row = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div("Sales Report"),
                width={"size": 6, "offset": 6},
            ),
        ),
        html.Hr(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("{} ".format(text)),
                    width={"size": 3, "order": 1, "offset": 1},
                ),
                dbc.Col(
                    html.Div("{}".format(text)),
                    width={"size": 3, "offset": 3},
                ),
            ]
        ),
        html.Hr(),
        html.Br(),
        dbc.Row(
            dbc.Col(
                html.Div(text),
                width={"size": 7, "offset": 3},
            ),
        ),
    ]
)

    rap = dbc.Container(
    [
              dbc.Col(
                 [
                     dcc.Graph(
                         figure={"data": [
                         {"x": x, "y": y},{"x": a, "y": b}
                         ],
                         "layout": dict(
            title='Sales data',
            showlegend=True,
            legend=dict(
                x=1,
                y=1
            ),
            margin=dict(l=40, r=0, t=40, b=30),
            hovermode='closest',
            transition = {'duration': 500},
        )
                         }
                            ),
                ],className="mt-4",
                ),
                ],
className="mt-4",
)
    button = html.Div(
    [
        dbc.Button("Create PDF file", id="example-button", className="btn btn-dark btn-lg"), 
        html.Span(id="example-output", style={"vertical-align": "middle", "margin-left":"50px"}),
    ], style={"margin-left": "50%"}
)
    
    layout = html.Div([
        nav,
        header,
        rap,
        html.Br(),
        html.Hr(),
        row,
        html.Br(),
        button

    ])
    return layout