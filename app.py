###
#Packages Dash
import dash
from dash import dcc
from dash import html
from dash import dash_table as dt
import dash_bootstrap_components as dbc
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

df_copy = df.copy()


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
            direction = "down",
            align_end=True,
            
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
    "width": "14rem",
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
<<<<<<< HEAD
        html.H2("Menu", className="display-4"),
=======
        html.H2("Sidebar", className="display-4"),
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
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
# Page Home (hello)
hello = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("Variação dos Preços dos Cereais ao Longo dos Últimos 30 Anos", style={'textAlign': 'center'}),
        html.Hr(),
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
    ],
    
)


###
<<<<<<< HEAD
# Page 1 (time series) - Control Panel + Graphics + Tabs

=======
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
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
controls_1 = dbc.Card(
    [
        
        html.Div(
            [
                dbc.Label("Variavel de Análise"),
                dcc.Dropdown(
                    id="variable_y_1",
                    options=[
                        {"label": col, "value": col} for col in df_copy.drop(['Inflation_rate'], axis = 1).columns[2:]
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

<<<<<<< HEAD
graph_1_tab1 = dbc.Container(
=======
graph_1 = dbc.Container(
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
    [
        html.H1("Séries Históricas - "),
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

page1_tab1_content = dbc.Card(
    dbc.CardBody(
        [
            graph_1_tab1
        ]
    ),
    className="mt-3",
)

page1_tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

page1 = html.Div(
   [
        dbc.Tabs(
            [
                dbc.Tab(page1_tab1_content, label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page1"),
                dbc.Tab(page1_tab2_content, label="Tab 2",
                        tab_id = "tab-2-page1",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page1"
        ),
        #html.Div(id="content"),
    ]
)


###
# Page 2 (boxplot) - Control Panel + Graphics + Tabs
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

graph_2_tab1 = dbc.Container(
    [
        html.H1("Boxplot - "),
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

page2_tab1_content = dbc.Card(
    dbc.CardBody(
        [
            graph_2_tab1
        ]
    ),
    className="mt-3",
)

page2_tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

page2 = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(page2_tab1_content, label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page2"),
                dbc.Tab(page2_tab2_content, label="Tab 2",
                        tab_id = "tab-2-page2",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page2"
        ),
        #html.Div(id="content"),
    ]
)

###
# Page 3 (histogram) - Control Panel + Graphics + Tabs
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

graph_3_tab1 = dbc.Container(
    [
        html.H1("Histograma - "),
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

page3_tab1_content = dbc.Card(
    dbc.CardBody(
        [
            graph_3_tab1
        ]
    ),
    className="mt-3",
)

page3_tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

page3 = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(page3_tab1_content, label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page3"),
                dbc.Tab(page3_tab2_content, label="Tab 2",
                        tab_id = "tab-2-page3",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page3"
        ),
        #html.Div(id="content"),
    ]
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
<<<<<<< HEAD
# Page 4 (About)

about = dbc.Container(
    [
        html.H1("Informações sobre o dataset"),
        html.Hr(),
        dcc.Markdown('''            
        Fonte: <https://www.kaggle.com/datasets/timmofeyy/-cerial-prices-changes-within-last-30-years>
                    '''),
    ],
    fluid=True,
)

page4_tab1_content = dbc.Card(
    dbc.CardBody(
        [
            about
        ]
    ),
    className="mt-3",
)

page4_tab2_content = dbc.Card(
    dbc.CardBody(
        [
        html.H1("Dataset"),
        html.Hr(),    
        dt.DataTable(data = df.to_dict("records"),
                            id="table",
                            columns=[{"name": i, "id": i} for i in df.columns],
                            page_current= 0,
                            page_size= 24,
                            style_cell={
                                            'overflow': 'hidden',
                                            'textOverflow': 'ellipsis',
                                            'maxWidth': 0,
                                        },
                            sort_action="native",
                            sort_mode='multi',
                    )
        ]
    ),
    className="mt-3",
)

page4 = html.Div(
=======
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
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
    [
        html.H1("Histograma"),
        html.Hr(),
        dbc.Row(
            [
<<<<<<< HEAD
                dbc.Tab(page4_tab1_content, label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page4"),
                dbc.Tab(page4_tab2_content, label="Tab 2",
                        tab_id = "tab-2-page4",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page4"
        ),
        #html.Div(id="content"),
=======
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
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
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
<<<<<<< HEAD
=======
                        #tabs,
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
                        content,
                    ]
                
                 ),
                 ]  
             ),   
                ],
                
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
<<<<<<< HEAD
        return [
            
                hello
            
        ]
    if pathname == "/page-1":
        return [
            
                page1
=======
        return [
            
                hello
            
        ]
    if pathname == "/page-1":
        return [
            
                graph_1
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
            
        ]
    elif pathname == "/page-2":
        return [
            
<<<<<<< HEAD
                page2
=======
                graph_2
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
            
        ]
    elif pathname == "/page-3":
        return [
            
<<<<<<< HEAD
                page3
=======
                graph_3
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
            
        ]
    elif pathname == "/page-4":
        return [
            
<<<<<<< HEAD
                page4
=======
                about
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
            
        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

<<<<<<< HEAD
=======
#@app.callback(
#    Output("content", "children"),
#    [Input("tabs", "active_tab")])
#def switch_tab(at):
#    if at == "tab-1":
#        return tab1_content
#    elif at == "tab-2":
#        return tab2_content
#    return html.P("This shouldn't ever be displayed...")

>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc

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
<<<<<<< HEAD
=======
    
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
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
<<<<<<< HEAD
    df_copy = df_copy.drop(['Month', 'Inflation_rate'], axis = 1)
           
=======
    
    df_copy = df_copy.drop(['Month', 'Inflation_rate'], axis = 1)
    
       
>>>>>>> 9601670b160d690b7e19a70b272478b2adaef3dc
    fig = px.histogram(df_copy, x = 'Price_rice_ton')
    
    return fig

    
###
# RUN

if __name__ == "__main__":
    app.run_server(debug=True, port=8086) 