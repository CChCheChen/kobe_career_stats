import pandas as pd
from dash import Dash, dcc, html, Input, Output

def stats_mapping(stats):
    stats_map = {
        'G': 'Games played',
        'FG': 'Field goal made per game',
        'FGA': 'Field goal attampts per game',
        'PTS': 'Points per game',
        'TRB': 'Rebounds per game',
        'AST': 'Assists per game',
        'STL': 'Steals per game',
        'BLK': 'Blocks per game',
        'FG%': 'Field goal percentage'
    }
    return stats_map.get(stats)


def filter_data(df_og):
    # Select the desired columns
    df = df_og[['Season', 'G', 'FG', 'FGA', 'TRB', 'AST', 'STL', 'BLK', 'PTS']]

    # Calculate new columns and add them to the DataFrame
    df['FG%'] = round(df['FG'] / df['FGA'], 2)
    df['Year'] = df['Season'].str[:4]

    df = df.iloc[:-1] # print(kb_reg)
    df['Year'] = pd.to_datetime(df['Year'])
    # df.assign(Year = lambda data: pd.to_datetime(data["Year"], format="%Y")).sort_values(by="Year")

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

first_season = str(kb_reg["Year"].min())[:4]
last_season = str(kb_reg["Year"].max())[:4]

marks = {i: str(i) for i in range(int(first_season), int(last_season), 5)}
marks[int(last_season)] = last_season

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
                            id="stats-type-filter",
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
                            id='season-range', 
                            min=int(first_season), 
                            max=int(last_season),
                            step=1,
                            value=int((int(last_season) + int(first_season)) / 2),
                            marks=marks,
                            className="slidebar",
                        ),
                    ]
                ),
            ],
            className="menu-bottom",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="pts-plot",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="g-plot",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    Output("pts-plot", "figure"), # points per game plot
    Output("g-plot", "figure"), # games played plot
    Input("regular-playoff-filter", "value"),
    Input("stats-type-filter", "value"),
    [Input("season-range", "value")],
)
def update_charts(regular_playoff, stats_type, end_season):
    
    if(regular_playoff == 'Regular Season') :
        data = kb_reg
    else :
        data = kb_po

    # data['Year'].apply(lambda x: int(str(x.strftime('%Y'))[:4]))

    end_season = pd.to_datetime(end_season, format="%Y")
    filtered_data = data.query("Year <= @end_season")

    print(filtered_data)

    stats_type_full = stats_mapping(stats_type)

    pts_plot_figure = {
        "data": [
            {
                "x": filtered_data["Year"],
                "y": filtered_data[stats_type],
                "type": "lines",
                "hovertemplate": "%{y:.2f} <br><extra></extra>" + stats_type_full,
            },
        ],
        "layout": {
            "title": {
                "text": stats_type_full + " of each season",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False},
            "yaxis": {"fixedrange": False},
            "colorway": ["#542581"],
        },
    }

    g_plot_figure = {
        "data": [
            {
                "x": filtered_data["Year"],
                "y": filtered_data["G"],
                "type": "lines",
                "hovertemplate": "%{y:.2f} Games played<extra></extra>"
            },
        ],
        "layout": {
            "title": {
                "text": "Game played of each season", 
                "x": 0.05, 
                "xanchor": "left"},
            # "xaxis": {"fixedrange": True},
            # "yaxis": {"fixedrange": True},
            "colorway": ["#FDB927"],
        },
    }
    return pts_plot_figure, g_plot_figure

if __name__ == "__main__":
    app.run_server(debug=True)