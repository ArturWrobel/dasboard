import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import smtplib, ssl
from email.message import EmailMessage

from navbar import Navbar

sender = "artur.r.wrobel@gmail.com"
receiver = "artur.wrobel@orange.com"
filename="test.pdf"

def email_send():
    msg = EmailMessage()
    msg["From"] = sender
    msg["Subject"] = "o co chodzi?"
    msg["To"] = receiver
    msg.set_content("This is the message body. This is the message body.")
    msg.add_attachment(open(filename, "r", errors='ignore').read(), filename="test.pdf")

    context=ssl.create_default_context()

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls(context=context)
    s.login("artur.r.wrobel@gmail.com", "EWing2015")
    s.send_message(msg)

def Send(r, t):
    try:
        if r == 0:
            t = "File sent to: {}".format(receiver)
            email_send()
            print ("załadowane!")
        else:
            print ("nie załadowane")
    except FileNotFoundError:
        t = "Please prepeare PDF file first"

    nav = Navbar()

    header = html.H3(
        '{}'. format(t)
    )

    layout = html.Div([
        nav,
        header,
    ])
    return layout