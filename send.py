import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import smtplib, ssl
from email.message import EmailMessage
from data import mailing

from navbar import Navbar

mailing_group = []

sender = "artur.r.wrobel@gmail.com"

filename="test.pdf"

#[email_send(i) for i in mailing_group]

def email_send(receiver):
    msg = EmailMessage()
    msg["From"] = sender
    msg["Subject"] = "Email created in Dash"
    msg["To"] = receiver
    msg.set_content("This is the message body. This is the message body.")
    msg.add_attachment(open(filename, "r", errors='ignore').read(), filename="test.pdf")
    
    context=ssl.create_default_context()

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls(context=context)
    s.login("artur.r.wrobel@gmail.com", "{}".format(mailing))
    s.send_message(msg)

import os
def Send(r, t):
    if r == 0:
        if os.path.exists("test.pdf"):
            t = "Report ready for distribution"
        else:
            t = "Please prepeare PDF file first"
    else:
        t = "Please download data first"


    nav = Navbar()

    header = html.H3(
        ['{}'. format(t)], style={"color": "red", "margin-top" : "100px", "margin-left" : "100px"}
    )

    a = "artur.wrobel@orange.com"
    b = "zdzislaw.filipowski1@orange.com"
    c = "artur.r.wrobel@gmail.com"
    d = "artur.raf.wrobel@gmail.com"


    email_choice = html.Div([
    dcc.Dropdown(
        id='email-dropdown',
        options=[
            {'label': 'Artur', 'value': a},
            {'label': 'Zdzislaw', 'value': b},
            {'label': 'Artur1', 'value': c},
            {'label': 'Artur2', 'value': d},
        ], style= {"width": "70%", "left": "100px" },
        multi=True,
    
    ),
    html.Br(),
    html.Br(),
    html.Div(id='email-container')
])

    sending = html.Div(
    [
        dbc.Button("Send report", id="send-button", className="btn btn-dark btn-lg"), 
        html.Span(id="send-output", style={"vertical-align": "middle", "margin-left":"50px"}),
    ], style={"margin-left": "100px"})

    layout = html.Div([
        nav,
        header,
        html.Br(),
        html.Br(),
        email_choice,
        html.Br(),
        html.Br(),
        sending

    ])
    return layout