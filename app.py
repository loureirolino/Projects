###
#Packages Dash
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# Others Packages
import plotly.express as px
import plotly.graph_objects as go
import numpy as np 
import pandas as pd


###
# Data
path = '/home/lucas/Downloads/'
name_df = 'rice_wheat_corn_prices.csv'

sheets_names = ['12 Nov', '13 Nov', '14 Nov']
col_names = ['time', 'chassis', 'laps', 'slick_rain', 'psi_fl', 'psi_fr', 'psi_rl', 'psi_rr',
             'obs', 'bar_fl', 'bar_fr', 'bar_rl', 'bar_rr', 'final_position', 'use_type']

for i in range(len(sheets_names)):
    globals()['df_%s' % i] = pd.read_excel(path + name_df, sheet_name = sheets_names[i], skiprows = 28,  usecols= 'A:O')
    globals()['df_%s' % i].columns = col_names


###
# Page Component - Navbar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 1", href="/page-1"),
                dbc.DropdownMenuItem("Page 2", href="/page-2"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple - Name",
    brand_href="#",
    color="primary",
    dark=True,
)

###
# Page Component - Sidebar

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    #"position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


###
# Page Component - Buttons


###
# page Component - Tabs
tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Tab 1", tab_id="tab-1"),
                dbc.Tab(label="Tab 2", tab_id="tab-2"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="content"),
    ]
)


###
# Dash - Page Layout

# Core Struture
app = dash.Dash(
    __name__, external_stylesheets = [dbc.themes.BOOTSTRAP],title = "Nome do App"
)

server = app.server

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(id="page-content", style=CONTENT_STYLE, className="pt-4")

app.layout = html.Div(   
        [
            dcc.Location(id="url"),
            navbar,
            dbc.Container(
                [
                    dbc.Row(
                 [
                 sidebar,
                 dbc.Col(
                    [
                        tabs,
                        content,
                    ]
                
                 ),
                 ]  
             ),   
                ]
            )    
            
        ],       
)

###
# Callbacks

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return [
            
                html.H1('Page 1'),
                html.P("This is the content of page 1!")
            
        ]
    elif pathname == "/page-2":
        return [
            
                html.H1('Page 2'),
                html.P("This is the content of page 2!")
            
        ]
    elif pathname == "/page-3":
        return [
            
                html.H1('Page 3'),
                html.P("This is the content of page 3!")
            
        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    return html.P("This shouldn't ever be displayed...")

    
###
# RUN

if __name__ == "__main__":
    app.run_server(debug=True, port=8086) 
