import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go

from fpdf import FPDF

from navbar import Navbar

nav = Navbar()

def pdf_rep():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Sales Report 21-02-2020", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.cell(50, 10, 'Sales', 1, 0, 'C')
    pdf.cell(40, 10, 'Costs', 1, 0, 'C')
    pdf.cell(40, 10, 'Items', 1, 2, 'C')
    pdf.cell(-90)
    pdf.set_font('arial', '', 12)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    pdf.image('orange.jpg', x = 40, y = 40, w = 0, h = 0, type = '', link = '')
    pdf.output('test.pdf', 'F')

def Report(r, t, df1):
    if r == 0:
        print ("załadowane!")
        #ti = pd.to_datetime(df1.data)
        #ti = ti.dt.date
        t = "Report is ready"
        x=[1,2,3,4,5,6,7,8,9]
        y=[8,1,7,4,5,3,1,6,8]
        text = "Average daily turnover during current month: 55.5 item"
    else:
        print ("nie załadowane")
        ti =[]
        x=[]
        y=[]
        text = ""
        
    header = html.H3(
        '{}'. format(t)
    )

    row = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div("{}".format(text)),
                width={"size": 6, "offset": 5},
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("{}".format(text)),
                    width={"size": 3, "order": "last", "offset": 1},
                ),
                dbc.Col(
                    html.Div("{}".format(text)),
                    width={"size": 3, "order": 1, "offset": 2},
                ),
                dbc.Col(
                    html.Div("{}".format(text)),
                    width={"size": 3, "order": 12},
                ),
            ]
        ),
    ]
)

    rap = dbc.Container(
    [
              dbc.Col(
                 [
                     dcc.Graph(
                         figure={"data": [{"x": x, "y": y}]}
                            ),
                ],
                ),
                ],
className="mt-4",
)
    button = html.Div(
    [
        dbc.Button("PDF file", id="example-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)
    
    layout = html.Div([
        nav,
        header,
        rap,
        html.Br(),
        html.Br(),
        html.Hr(),
        html.Br(),
        html.Br(),
        row,
        html.Br(),
        html.Br(),
        button


    ])
    return layout