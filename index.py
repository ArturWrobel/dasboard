import base64
import datetime
import io
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import App, build_graph
from charts import Charts
from report import Report, pdf_rep
from send import Send, email_send
from apka import Apka
from download import Download
from home import Home

import dash_table

import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Links to CSS, JS
external_stylesheets = [
    dbc.themes.UNITED,
    
]
df1 = []
r = 1
t = "Please download data first"

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

# Callback to chose page

x=[]
z=[]
text = "Please download data first"

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/download':
        return Download()
    elif pathname == '/app':
        return App()
    elif pathname == '/apka':
        return Apka(x,z, text)
    elif pathname == '/charts':
        return Charts(r, t, df1)
    elif pathname == '/report':
        return Report(r, t, df1)
    elif pathname == '/send':
        return Send(r, t)
    else:
        return Home()

# Callback (App)
@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)

def update_graph(city):
    graph = build_graph(city)
    return graph

# Callback (Chart)

@app.callback(
    Output('gra', 'figure'),
    [Input('daty-slider', 'value')])
def up(figure):
    
    if r == 1:
        od = 0
        do = 0
        data = []
    else:
        df1.data = pd.to_datetime(df1.data)
        df1.data = df1.data.dt.date
        dat = df1.data[figure[0]:(figure[1]+1)].tolist()
        g = df1.index[figure[0]:(figure[1]+1)].tolist()
        dat = [dat[i].strftime('%d/%m/%Y') for i in range(len(g))]
        
        print("figures ",figure[0]," and ", figure[1])
        od = df1["data"][figure[0]]
        
        do = df1["data"][figure[1]-1]
        print("od: ", od, " do: ",do)

        data = [
        dict(
            x = dat,
            y = [df1["costs"][i] for i in g],
            name = "costs"
        ),
        dict(
            x = dat,
            y = [df1["sold"][i] for i in g],
            name = "sold"
        ),
        dict(
            x = dat,
            y = [df1["result"][i] for i in g],
            name = "result"
        ),
        dict(
            x = dat,
            y = [df1["cumulated"][i] for i in g],
            name = "cumulated"
        )
    ]

    return {"data": data,
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

# Callback Prepeare PDF file

@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if r == 0:
        if n is None:
            return "Please push button to prepeare PDF file"
        else:
            pdf_rep()      
            return "PDF file is ready"
    else:
        return "Please download data first"

# Reading file

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            print(df)   
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            global df1
            df1 = df
            global x
            x = pd.to_datetime(df.data)
            x = x.dt.date
            global z
            y = df['data'].dt.date
            z = df.costs

            global text
            text = ""

            layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')
            fig = go.Figure()
            #fig = go.Figure(data = [{"x": x, "y": df.costs}], layout = layout)
            fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5], y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]))
            fig.add_trace(go.Bar(x=[0, 1, 2, 3, 4, 5], y=[5, 5, 7, 4, 1, 3]))  
            global r
            r = 0
            global t
            t = "Download succesful :)"       
            
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),
                     html.H2("Graph of:"),
                     dcc.Graph(id='e-graph',
                         figure={"data": [{"x": x, "y": df.costs},
                         {"x": x, "y": df.sold, 'type': 'line', 'fillcolor': 'rgba(68, 68, 68, 0.1)', 'fill': 'tonexty', 'line': {'width': 2}, 'name': 'Upper Pred', 'showlegend': True, 'hoverinfo': 'none'},
                         {"x": x, "y": df.result, 'type': 'bar'},
                         {"x": x, "y": df.cumulated},
                         ]}
                            ),
        html.P([
                    html.Label("Time Period"),
                    dcc.RangeSlider(id = 'sliderx',
                                    #marks = {i : y[i] {‘label’ : available_dates_rangeslider[i], ‘style’:{‘transform’:‘rotate(-90deg)’, ‘font-size’:‘8px’}} for i in range(len(y))},
                                    marks={i : {'label' : y[i], 'style':{'transform':'rotate(-90deg)', 'font-size':'15px'}} for i in range(0, len(y)) if i %2 ==0},
                                    min = 1,
                                    max = len(x),
                                    value = [1, len(y)-2])
                        ], style = {'width' : '80%',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
                                    dcc.Graph(id = 'plot', figure = fig),
                    
    ])

# Callback for Apka

@app.callback(Output('outputt', 'figure'),
             [Input('slider', 'value')])

def update_figure(value):
    print(77)

    return print("zzzzzzzzzzzzzzzzzzz", value[0], value[1], "razem ", value)
 
# Callback to download file

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
               
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(debug=False)