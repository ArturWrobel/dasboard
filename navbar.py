import dash_bootstrap_components as dbc
import dash_html_components as html

def Navbar():
   navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Download", href="/download")),
              dbc.NavItem(dbc.NavLink("App", href="/app")),
              dbc.NavItem(dbc.NavLink("Apka", href="/apka")),
              dbc.NavItem(dbc.NavLink("Charts", href="/charts")),
              dbc.NavItem(dbc.NavLink("Report", href="/report")),
              dbc.NavItem(dbc.NavLink("Send", href="/send")),
                    ],
          brand="Orange Finance",
          brand_href="/home",
          sticky="top",
          
        )
   return navbar