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
url ='https://raw.githubusercontent.com/loureirolino/Projects/master/rice_wheat_corn_prices.csv'

df = pd.read_csv(url)

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
                dbc.DropdownMenuItem("Boxplot", href="/page-2"),
                dbc.DropdownMenuItem("Histograma", href="/page-3"),
                dbc.DropdownMenuItem("Sobre", href="/page-4"),
            ],
            nav=True,
            in_navbar=True,
            label="Mais",
        ),
    ],
    brand="Navbar",
    brand_href="#",
    color="primary",
    dark=True,
)

###
# Page Component - Sidebar
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
            "Categorias", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Página Inicial", href="/", active="exact"),
                dbc.NavLink("Série Histórica", href="/page-1", active="exact"),
                dbc.NavLink("Boxplot", href="/page-2", active="exact"),
                dbc.NavLink("Histograma", href="/page-3", active="exact"),
                dbc.NavLink("Sobre", href="/page-4", active="exact"),
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
# Page Home (hello)
hello = dbc.Container(
    [
        html.H1("Variação dos Preços dos Cereais ao longo dos últimos 30 anos"),
        html.Br(),
        dcc.Markdown('''            
        ## Projeto Final de APC - 2021.2  \
                
        ### Universidade de Brasília - Departamento de Ciência da Computação
                    '''),
        html.Br(),
        dcc.Markdown(''' 
        ### Alunos:
        * Lucas Loureiro Lino da Costa
                    ''' )
    ]
)

###
# Page 1 (time series) - Control Panel + Graphics
controls_1 = dbc.Card(
    [
        
        html.Div(
            [
                dbc.Label("Variavel de Análise"),
                dcc.Dropdown(
                    id="variable_y_1",
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
                    id="variable_x_1",
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

graph_1 = dbc.Container(
    [
        html.H1("Séries Históricas"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls_1, md=4),
                dcc.Graph(id="series-graph"),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


###
# Page 2 (boxplot) - Control Panel + Graphics
controls_2 = dbc.Card(
    [
        
        html.Div(
            [
                dbc.Label("Ano de Análise"),
                dcc.Dropdown(
                    id="variable_x_2",
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

graph_2 = dbc.Container(
    [
        html.H1("Boxplot"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls_2, md=4),
                dcc.Graph(id="boxplot-graph"),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


###
# Page 3 (histogram) - Control Panel + Graphics
controls_3 = dbc.Card(
    [
        
        html.Div(
            [
                dbc.Label("Ano de Análise"),
                dcc.Dropdown(
                    id="variable_x_3",
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

graph_3 = dbc.Container(
    [
        html.H1("Histograma"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls_3, md=4),
                dcc.Graph(id="histogram-graph"),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


###
# Page 4 (About)
about = dbc.Container(
    [
        html.H1("Informações sobre o dataset"),
        dcc.Markdown('''            
        Fonte: <https://www.kaggle.com/datasets/timmofeyy/-cerial-prices-changes-within-last-30-years>
                    '''),
    ]
)

###
# page Component - Tabs
#tabs = html.Div(
#    [
#        dbc.Tabs(
#            [
#                dbc.Tab(label="Tab 1", tab_id="tab-1"),
#                dbc.Tab(label="Tab 2", tab_id="tab-2"),
#            ],
#            id="tabs",
#            active_tab="tab-1",
#        ),
#        html.Div(id="content"),
#    ]
#)




###
# Dash - Page Layout

# Core Struture
app = dash.Dash(
    __name__, external_stylesheets = [dbc.themes.BOOTSTRAP],title = "painel_grupo_10"
)

server = app.server

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
                        #tabs,
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

# Page redirections
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            
                hello
            
        ]
    if pathname == "/page-1":
        return [
            
                graph_1
            
        ]
    elif pathname == "/page-2":
        return [
            
                graph_2
            
        ]
    elif pathname == "/page-3":
        return [
            
                graph_3
            
        ]
    elif pathname == "/page-4":
        return [
            
                about
            
        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

#@app.callback(
#    Output("content", "children"),
#    [Input("tabs", "active_tab")])
#def switch_tab(at):
#    if at == "tab-1":
#        return tab1_content
#    elif at == "tab-2":
#        return tab2_content
#    return html.P("This shouldn't ever be displayed...")


# Page 1 - graphic output
@app.callback(
    Output("series-graph", "figure"),
    [
        Input("variable_x_1", "value"),
        Input("variable_y_1", "value"),
    ],
)
def make_graph(x, y):
    
    df_copy = df.copy()
    df_copy = df_copy[(df_copy.Year == x)]
    cols = ['Year', 'Month', y]
    
    
    # Option 1
    #df_copy = df_copy[df_copy.columns.intersection(cols)]
    
    # Option 2
    #df_copy = df_copy[df_copy.columns & cols]
    
    # Option 3
    data = []
    for col in cols:
        data.append(list(df_copy[col]))
    df_copy = pd.DataFrame({cols[i]: data[i] for i in range(3)})


    fig = px.line(
            df_copy,
            x = 'Month',
            y = y,
            markers = True,
            labels = {'Price_wheat_ton':'Preço em US$ para a <br> tonelada de trigo',
                    'Price_rice_ton' : 'Preço em US$ para a <br> tonelada de arroz',
                    'Price_corn_ton' : 'Preço em US$ para a <br> tonelada de milho',
                    'Inflation_rate': 'Taxa de inflação <br> (ano base = 1992)',
                    'Price_wheat_ton_infl' : 'Preço em US$ para a <br> tonelada de trigo (corrigido pela inflação',
                    'Price_rice_ton_infl' : 'Preço em US$ para a <br> tonelada de arroz (corrigido pela inflação)',
                    'Price_corn_ton_infl' : 'Preço em US$ para a <br> tonelada de milho (corrigido pela inflação)',
                    'Month' : 'Mês de Análise'}
            )
                    

    return fig

# Page 2 - graphic output
@app.callback(
    Output("boxplot-graph", "figure"),
    [
        Input("variable_x_2", "value")  
    ],
)
def make_graph(x):
    df_copy = df.copy()
    df_copy = df_copy[(df_copy.Year == x)]
    
    df_copy = df_copy.drop(['Month', 'Inflation_rate'], axis = 1)
    
    legend_names = ['Preço em US$ para a <br> tonelada de trigo', 'Preço em US$ para a <br> tonelada de arroz',
                    'Preço em US$ para a <br> tonelada de milho', 'Preço em US$ para a <br> tonelada de trigo (corrigido pela inflação',
                    'Preço em US$ para a <br> tonelada de milho (corrigido pela inflação)']
    
    fig = go.Figure()
    for col in df_copy.iloc[:, 1:]:
        fig.add_trace(go.Box(y = df_copy[col].values,
                             name = df_copy[col].name)
                      )
    fig.update(layout_xaxis_visible = False)
    
    return fig


# Page 3 - graphic output
@app.callback(
    Output("histogram-graph", "figure"),
    [
        Input("variable_x_3", "value"),
    ],
)
def make_graph(x):
    df_copy = df.copy()
    df_copy = df_copy[(df_copy.Year == x)]
    
    df_copy = df_copy.drop(['Month', 'Inflation_rate'], axis = 1)
    
       
    fig = px.histogram(df_copy, x = 'Price_rice_ton')
    
    return fig

    
###
# RUN

if __name__ == "__main__":
    app.run_server(debug=True, port=8086) 