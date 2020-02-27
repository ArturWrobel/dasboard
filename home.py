import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from navbar import Navbar

nav = Navbar()

# Fig0


fig0 =go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
), )

    
fig0.update_layout(margin = dict(t=0, l=0, r=0, b=0), paper_bgcolor='rgb(248, 248, 255)',)

# Fig1

fig1 = go.Figure(data=[go.Pie
(labels= ["A","B","C","D"], values=[4500, 2500, 1500, 1100], pull=[0, 0.2, 0, 0])])

colors1 = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

fig1.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors1, line=dict(color='#000000', width=2)))

fig1.update_layout(paper_bgcolor='rgb(248, 248, 255)')

# Fig

top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
              'Strongly<br>disagree']

colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']

x_data = [[21, 30, 21, 16, 12],
          [24, 31, 19, 15, 11],
          [27, 26, 23, 11, 13],
          [29, 24, 15, 18, 14]]

y_data = ['This app is interesting<br>and will give a try',
          'The app will help in my<br>daily workflow ' +
          'and<br> speeds up things', 'The app is annoying' +
          'and<br>I will never use it<br>again',
          'I would recommend this<br>application to colegues']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

body = dbc.Container(
    [  dbc.Row([html.H1("Finance Dasboard")]),
       dbc.Row([html.P("Web application based on Dash framework to analyse financial data downloaded from Excell.")]),
       dbc.Row(
           [
               dbc.Col(
                  [
                     #html.H2("Graphic presentation"),
                     dcc.Graph(
                        figure={"data": [{"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14], "y": [1, 1, 9,8,11,15,17,14,12,12,7,6,10,14], 'name': 'data-1'},
                                         {"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14], "y": [2,5, 5,5,1,1,-2,7,5,2,9,9,5,6],'type': 'bar', 'name': 'data-2'}],
                                'layout': {'title': 'Dash Data Visualization Examples', 'backgroundColour' : "rgb(248, 248, 255)"},
                        },
                        style={
                        'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '10px'
        },
                            ),
                        ],
                  md=6,
               ),
              dbc.Col(
                 [
                     #html.H2("Graphic presentation"),
                     dcc.Graph(
                        figure={"data": [{"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14], "y": [1, 1, 9,8,11,15,17,14,12,12,7,6,10,14], 'name': 'data-1'},
                                         {"x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14], "y": [2,5, 5,5,1,1,-2,7,5,2,9,9,5,6], 'name': 'data-2'}],
                                'layout': {'title': 'Dash Data Visualization Examples'},
                        },
                        style={
                        'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '10px'
        },
                            ),
                        ],
                        
                     ),
                ]
                
            ),
            dbc.Row([
                dbc.Col([
                dcc.Graph(
                        figure=fig0
                        ,
                        style={
                        'borderWidth': '1px',
            'borderStyle': 'solid',
            'textAlign': 'center',
            'margin': '10px'
        },
                            ),
                ], md = 6),
                dbc.Col([
                dcc.Graph(
                        figure=fig1,
                        style={
                        'borderWidth': '1px',
            'borderStyle': 'solid',
            'textAlign': 'center',
            'margin': '10px'
        },
                            ),
                ])
            ]),
            dbc.Row([
                dcc.Graph(
                        figure=fig
                        ,
                        style={
                        'borderWidth': '1px',
            'borderStyle': 'solid',
            'textAlign': 'center',
            'margin-left': '25px',
            'margin-right': '25px',
            'margin-top': '10px',
            "width" : "100%"
        },
                            ),
            ])
       ],
className="mt-4",
)

def Home():
    layout = html.Div([
    nav,
    body
    ])
    return layout