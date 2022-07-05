import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP],
                 meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
app.layout = dbc.Container([

    dbc.Col(html.H1('Term Structure Rate Interest',
            className = 'text-center'),
            width = 12) # end first row


]) #end layout
if __name__ == '__main__':
    app.run_server(debug = True, port =6969)
