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

df_copy = df.copy()
df_copy.Month = df_copy.Month.replace(old_month, new_month)


###
# Page Component - Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.Button("Menu", outline=True, color="primary", className="mr-1", id="btn_sidebar"),
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
    brand="brand",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)


###
# Page Component - Sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa"
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
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
    id="sidebar",
    style=SIDEBAR_STYLE,
)

###
# Start Page (hello/about)
hello = dbc.Card(
    [
        dbc.Container(
        [
            html.H1("Variação dos Preços dos Cereais ao Longo dos Últimos 30 Anos", style={'textAlign': 'center'}),
            html.Hr(),
            html.Div(
                [
                    dcc.Markdown('''            
            ## Projeto Final de APC - 2021.2  \
                    
            ### Universidade de Brasília - Departamento de Ciência da Computação
                        '''),
            html.Br(),
            dcc.Markdown(''' 
            ### Aluno:
            * Lucas Loureiro Lino da Costa
                        ''' )
                ]
            ),   
        ]
        ),  
    ],
)


###
# Page 1 (time series) - Control Panel + Graphics + Tabs
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

graph_1_tab1 = dbc.Container(
    [
        html.H1("Séries Históricas - Duplo Corte por Variável e Ano"),
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
                dbc.Tab(page1_tab1_content,
                        label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page1"),
                dbc.Tab(page1_tab2_content,
                        label="Tab 2",
                        tab_id = "tab-2-page1",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page1"
        ),
        html.Div(id="content"),
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
        html.H1("Boxplot - Corte por Ano"),
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
                dbc.Tab(page2_tab1_content,
                        label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page2"),
                dbc.Tab(page2_tab2_content,
                        label="Tab 2",
                        tab_id = "tab-2-page2",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page2"
        ),
        html.Div(id="content"),
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
                dbc.Tab(page3_tab1_content,
                        label = "Tab 1",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page3"),
                dbc.Tab(page3_tab2_content,
                        label="Tab 2",
                        tab_id = "tab-2-page3",
                        active_label_style = {"color": "#FB79B3"}),
            ],
            active_tab= "tab-1-page3"
        ),
        html.Div(id="content"),
    ]
)


###
# Page 4 (About)
about = dbc.Container(
    [
        html.H1("Informações Sobre o Conjunto de Dados"),
        html.Hr(),
        dcc.Markdown('''
                     
        Série histórica da evolução dos preços dos cereais (arroz, milho e trigo) nos Estados Unidos nos últimos trinta (30) anos, de 1992 até o ano atual.  
        
        Os preços se encontram em dolares americanos (US$), assim como os dados são atualizados periodicamente pelo gestor do dataset.
        
        ## Variáveis do Conjunto de Dados:
        * Year - Ano de análise;
        * Month - Mês de análise;
        * Price_wheat_ton - Preço para a tonelada de trigo;
        * Price_rice_ton - Preço para a tonelada de arroz;
        * Price_corn_ton - Preço para a tonelada de milho;
        * Inflation_rate - Taxa de inflação apresentada no período;
        * Price_rice_ton_infli - Preço para a tonelada de arroz corrigido pela inflação do período;
        * Price_corn_ton_infli - Preço para a tonelada de milho corrigido pela inflação do período;
        * Price_wheat_ton_infli - Preço para a tonelada de trigo corrigido pela inflação do período;
        
        
        __Para mais informações acesse o link abaixo:__               
        __Fonte:__ <https://www.kaggle.com/datasets/timmofeyy/-cerial-prices-changes-within-last-30-years>
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
        ],
    ),
    className="mt-3",
)

page4 = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(page4_tab1_content,
                        label = "Infomações",
                        tab_style = {"marginLeft": "auto"},
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-1-page4"),
                dbc.Tab(page4_tab2_content,
                        label="Dataset",
                        active_label_style = {"color": "#FB79B3"},
                        tab_id = "tab-2-page4"),
            ],
            active_tab= "tab-1-page4",
        ),
        html.Div(id="content"),
    ],
    
)

###
# Dash - Core Struture
app = dash.Dash(
    __name__, external_stylesheets = [dbc.themes.BOOTSTRAP],
    title = "painel_dash_cereais"
)

server = app.server

content = html.Div(
    id="page-content",
    style=CONTENT_STYLE,
    className="pt-4"
    )

app.layout = html.Div(   
        [
            dcc.Store(id='side_click'),
            dcc.Location(id="url"),
            navbar,
            sidebar,
            content,
        ],
             
)

###
# Callbacks

# Sidebar
@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]

# Page redirections
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
    )
def render_page_content(pathname):
    if pathname == "/":
        return hello
    if pathname == "/page-1":
        return page1    
    elif pathname == "/page-2":
        return page2      
    elif pathname == "/page-3":
        return page3
    elif pathname == "/page-4":
        return page4 
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Page 1 - graphic 1 output
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

# Page 2 - graphic 1 output
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

# Page 3 - graphic 1 output
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