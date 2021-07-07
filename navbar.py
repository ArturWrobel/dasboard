import dash_bootstrap_components as dbc
import dash_html_components as html

def Navbar():
    PLOTLY_LOGO = "https://upload.wikimedia.org/wikipedia/commons/c/c8/Orange_logo.svg"

    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button("Search", color="primary", className="ml-2"),
                width="auto",
            ),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="40px")),
                        dbc.Col(dbc.NavbarBrand("Orange Finance", className="ml-2", style ={"color" : "white"})),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            
              dbc.NavItem(dbc.NavLink("Download", href="/download",  className="ml-5")),
              dbc.NavItem(dbc.NavLink("Table", href="/table")),
              dbc.NavItem(dbc.NavLink("App", href="/app")),
              dbc.NavItem(dbc.NavLink("Apka", href="/apka")),
              dbc.NavItem(dbc.NavLink("Charts", href="/charts")),
              #dbc.NavItem(dbc.NavLink("Calculate", href="/calc")),
              dbc.NavItem(dbc.NavLink("Report", href="/report")),
              dbc.NavItem(dbc.NavLink("Send", href="/send")),
        ],
        color="secondary",
        
        style = {"color" : "#AEA79F", "font-weight" : "700"},
        sticky="top",
        className="mt-1 ml-1 mr-1"
        )
    return navbar