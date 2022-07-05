import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
from yield_curve import Yield_Curve as yc

yc = yc()
df = yc.data
last_date = df.index[-1]

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SLATE],
                 meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

card_main = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Learn Dash with Charming Data", className="card-title"),
                html.H6("Lesson 1:", className="card-subtitle"),
                html.P(
                    "Choose the year you would like to see on the bubble chart.",
                    className="card-text",
                ),
                dcc.Input(
            id='my-input-day',
            type='number',
            value = 1,
            min=1, 
            step=1,
            className = 'form-control form-control-lg bg-primary text-white border border-dark')
            ]
        ),
    ],
    color="dark",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
)



app.layout = dbc.Container([

    dbc.Row(dbc.Col(html.H1('Term Structure Rate Interest',
            className = 'text-center'),
            width = 12)), # end first row
    dbc.Row([
        dbc.Col(
        dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=datetime.date(1961, 6, 14),
        initial_visible_month=last_date,
        className = 'bg-primary text-white')

        ), #end first column second row
        
        dbc.Col(
            dcc.Input(
            id='my-input-day',
            type='number',
            value = 1,
            min=1, 
            step=1,
            className = 'form-control form-control-lg bg-primary text-white border border-dark')
        ) # end second column second row

    ]), # end second row
    dbc.Row(
    dbc.Col(
        dcc.Graph(id='my-curve', figure={})
        ),#End col    
    className = 'm-5 bg-primary d-inline-block') # End third row

]) #end layout

@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='Date', y='High')
    return figln


if __name__ == '__main__':
    app.run_server(debug = True, port =6969)
