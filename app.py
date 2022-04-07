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

df = pd.read_csv(path + name_df)

new_month = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
old_month = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']

df.Month = df.Month.replace(old_month, new_month)


###
# Page Component - Navbar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Página Inicial", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Mais páginas", header=True),
                dbc.DropdownMenuItem("Série Histórica", href="/page-1"),
                dbc.DropdownMenuItem("Sobre", href="/page-2"),
                #dbc.DropdownMenuItem("Algo Mais", href="/page-3"),
            ],
            nav=True,
            in_navbar=True,
            label="Mais",
        ),
    ],
    brand="Variação dos Preços dos Seriais ao longo dos últimos 30 anos",
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
        html.H2("Projeto APC", className="display-4"),
        html.Hr(),
        html.P(
            "Categorias", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Página Inicial", href="/", active="exact"),
                dbc.NavLink("Série Histórica", href="/page-1", active="exact"),
                dbc.NavLink("Sobre", href="/page-2", active="exact"),
                #dbc.NavLink("Algo mais", href="/page-3", active="exact"),
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
# Page Component - Control Panel + Graphics
controls = dbc.Card(
    [
        
        html.Div(
            [
                dbc.Label("Variavel de Análise"),
                dcc.Dropdown(
                    id="variable_y",
                    options=[
                        {"label": col, "value": col} for col in df.columns[2:]
                    ],
                    value="Price_rice_ton",
                ),
            ]
        ),

        html.Div(
            [
                dbc.Label("Ano de Análise"),
                dcc.Dropdown(
                    id="variable_x",
                    options=[
                        {"label": entrie, "value": entrie} for entrie in df.Year.unique()    
                    ],
                    value=2019,
                ),
            ]
        ),
        
    ],
    body=True,
)

graph = dbc.Container(
    [
        html.H1("Séries Históricas"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dcc.Graph(id="series-graph"),
            ],
            align="center",
        ),
    ],
    fluid=True,
)



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
            
                graph
            
        ]
    elif pathname == "/page-2":
        return [
            
                html.H1("Informações sobre o dataset"),
                dcc.Markdown('''
                    


                    Fonte: <https://www.kaggle.com/datasets/timmofeyy/-cerial-prices-changes-within-last-30-years>
                    ''')
            
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



@app.callback(
    Output("series-graph", "figure"),
    [
        Input("variable_x", "value"),
        Input("variable_y", "value"),
    ],
)
def make_graph(x, y):
    
    df_copy = df.copy()
    df_copy = df_copy[(df_copy.Year == x)]
    cols = ['Year', 'Month', y]

    #Opt. 1
    data = []
    for col in cols:
        data.append(list(df_copy[col]))
    df_copy = pd.DataFrame({cols[i]: data[i] for i in range(3)})
       

    #Opt.2
    #df_copy[df_copy.columns & cols]

   
    fig = px.line(
            df_copy,
            x = 'Month',
            y = y,
            markers = True,
            labels = {'Price_wheat_ton':'Preço em US$ para a <br> tonelade de trigo',
                    'Price_rice_ton' : 'Preço em US$ para a <br> tonelade de arroz',
                    'Price_corn_ton' : 'Preço em US$ para a <br> tonelade de milho',
                    'Inflation_rate': 'Taxa de inflação <br> (ano base = 1992',
                    'Price_wheat_ton_infl' : 'Preço em US$ para a <br> tonelade de trigo (corrigo pela inflação',
                    'Price_rice_ton_infl' : 'Preço em US$ para a <br> tonelade de arroz (corrigo pela inflação)',
                    'Price_corn_ton_infl' : 'Preço em US$ para a <br> tonelade de milho (corrigo pela inflação)',
                    'Month' : 'Mês de Análise'})
                    

    return fig


    
###
# RUN

if __name__ == "__main__":
    app.run_server(debug=True, port=8086) 
