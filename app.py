import pandas as pd
from dash import Dash, dcc, html

def filter_data(df_og):
    # Select the desired columns
    df = df_og[['Season', 'G', 'FG', 'FGA', 'TRB', 'AST', 'STL', 'BLK', 'PTS']]

    # Calculate new columns and add them to the DataFrame
    df['FG%'] = round(df['FG'] / df['FGA'], 2)
    df['Year'] = df['Season'].str[:4]

    df = df.iloc[:-1] # print(kb_reg)
    df.assign(Year = lambda data: pd.to_datetime(data["Year"], format="%Y")).sort_values(by="Year")

    years = df["Year"].sort_values().unique()
    seasons = df["Season"].sort_values().unique() #print(seasons_reg)
    stat_cats = df.columns.drop(['Season', 'Year']) #print(stat_cats_reg)

    return df, years, seasons, stat_cats

kb_reg_og = pd.read_csv("kobe_stats_reg.csv")
kb_reg, years_reg, seasons_reg, stat_cats_reg = filter_data(kb_reg_og)
# print(kb_reg)

kb_po_og = pd.read_csv("kobe_stats_playoff.csv")
kb_po, years_po, seasons_po, stat_cats_po = filter_data(kb_po_og)

regular_playoff = ['Regular Season', 'Playoff']

marks = {i: str(i) for i in range(int(kb_reg["Year"].min()), int(kb_reg["Year"].max()) + 1, 5)}
marks[int(kb_reg["Year"].max())] = kb_reg["Year"].max()
print(marks)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
    {
        "href": (
            "https://codepen.io/chriddyp/pen/bWLwgP.css"
        ),
        "rel": "stylesheet",
    },
    {
        "href": (
            "'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src='assets/img/kobe-logo.jpeg', className="header-img"),
                html.P(children="🏀", className="header-emoji"),
                html.H1(
                    children="Kobe Career Stats Analytics Dashboard", className="header-title"
                ),
                html.P(
                    children=[
                        html.Span("Analyze Kobe Bryant's Career Game Stats from different seasons", className="header-text",),
                        html.Span("(Data available from 1996-97 to 2015-16 NBA regular seasons)", className="header-text",)
                    ],
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Regular Season/Playoff", className="menu-title"),
                        dcc.Dropdown(
                            id="regular-playoff-filter",
                            options=[
                                {
                                    "label": rp, 
                                    "value": rp}
                                for rp in regular_playoff
                            ],
                            value=regular_playoff[0],
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Stats Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {
                                    "label": sc,
                                    "value": sc,
                                }
                                for sc in stat_cats_reg
                            ],
                            value="PTS",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu-top",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children="Season Range", className="menu-title-bar"
                        ),
                        dcc.Slider(
                            id='xslider', 
                            min=int(kb_reg["Year"].min()), 
                            max=int(kb_reg["Year"].max()),
                            step=1,
                            value=int(kb_reg["Year"].min()),
                            marks=marks,
                            className="slidebar",
                        ),
                    ]
                ),
            ],
            className="menu-bottom",
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            figure={
                                "data": [
                                    {
                                        "x": kb_reg["Season"],
                                        "y": kb_reg["PTS"],
                                        "type": "lines",
                                    },
                                ],
                                "layout": {"title": "Points per game of each season"},
                            },
                            className="pts_plot",
                        ),
                    ],
                    className="col col-sm-12 col-md-12 col-lg-6 col-xl-6",
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            figure={
                                "data": [
                                    {
                                        "x": kb_reg["Season"],
                                        "y": kb_reg["G"],
                                        "type": "lines",
                                    },
                                ],
                                "layout": {"title": "Game played of each season"},
                            },
                            className="g_plot",
                        ),
                    ],
                    className="col col-sm-12 col-md-12 col-lg-6 col-xl-6",
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)