'''
Colombia Covid Dashboard

pip install dash
pip install dash_bootstrap_components

https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/

https://dev.socrata.com/foundry/www.datos.gov.co/gt2j-8ykr
https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data
https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F01ls2&gl=US&ceid=US%3Aen

'''
import dash
import requests
import pandas as pd
import json
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import pandas as pd
from sodapy import Socrata

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="primary", outline=True)),
        dbc.Col(dbc.Card(card_content, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content, color="info", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="success", outline=True)),
        dbc.Col(dbc.Card(card_content, color="warning", outline=True)),
        dbc.Col(dbc.Card(card_content, color="danger", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="light", outline=True)),
        dbc.Col(dbc.Card(card_content, color="dark", outline=True)),
    ]
)

cards = html.Div([row_1, row_2, row_3])

app.layout = html.Div([cards])


def accessDataViaCSV():
    url="https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&api_foundry=true"
    # url="Casos_positivos_de_COVID-19_en_Colombia.csv"
    df = pd.read_csv(url)

    # Print columns
    print(list(df.columns))

    # Preview the first 5 lines of the loaded data 
    index = df.index
    number_of_rows = len(index)
    print(f"Casos Confirmados = {number_of_rows}")

    df_recuperados = df[df["atención"] == "Recuperado"]
    print(f"Recuperados = {len(df_recuperados.index)}")

    df_fallecidos = df[df["Estado"] == "Fallecido"]
    print(f"Fallecidos = {len(df_fallecidos.index)}")

def accessDataViaSocrata():
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("www.datos.gov.co", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(www.datos.gov.co,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("gt2j-8ykr", limit=200000)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    df = results_df

    index = df.index
    number_of_rows = len(index)
    print(f"Casos Confirmados = {number_of_rows}")

    df_recuperados = df[df["atenci_n"] == "Recuperado"]
    print(f"Recuperados = {len(df_recuperados.index)}")

    df_fallecidos = df[df["estado"] == "Fallecido"]
    print(f"Fallecidos = {len(df_fallecidos.index)}")

if __name__ == "__main__":
    # app.run_server()
    accessDataViaSocrata()