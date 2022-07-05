


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
                html.H4("Choose a maturity in days", className="card-title"),
                dcc.Input(
            id='my-input-day',
            type='number',
            value = 1,
            min=1, 
            step=1,
            className = 'form-control form-control-lg bg-primary text-white border border-dark'),
            html.P(
                "The rate for the maturity selected is:.",
                className="card-text",
            ),            
            html.H4(id='my-output', className="card-title"),
            dbc.CardLink("Paper from FED", href="https://www.federalreserve.gov/pubs/feds/2006/200628/200628pap.pdf", target="_blank"),
            ]
        ),
    ],
    color="dark",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
)

card_graph = dbc.Card(
    [

        dbc.CardBody(
            [
        dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=datetime.date(1961, 6, 14),
        initial_visible_month=last_date,
        date=last_date,
        className = 'bg-primary text-white'),
        dcc.Graph(id='my-curve', figure={}, style = {'bgcolor':'black'})

            ]
        ),
    ],
    color="dark",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
)

        
app.layout = dbc.Container([

    dbc.Row(dbc.Col(html.H1('The U.S. Treasury Yield Curve',
            className = 'text-center'),
            width = 12)), # end first row
    
    dbc.Row([
        dbc.Col(card_main, width = 3),
        dbc.Col(card_graph, width = 9)

    ]) # end second row

]) #end layout


#---- callbacks -----

@app.callback(
    Output('my-curve', 'figure'),
    Input('my-date-picker-single', 'date')
)
def update_graph(date_value):
    curve  = yc.svensson_curve(date = pd.Timestamp(date_value))
    df = pd.DataFrame()
    df['days'] = [i for i in range(1,len(curve)+1)]
    df['rate'] =  curve
    figln = px.line(df, x = 'days', y = 'rate')
    figln.update_layout(plot_bgcolor='#2F3132', 
    paper_bgcolor = '#2F3132',
    font_color = 'white',
    hoverlabel_bgcolor = '#2F3132')
    return figln

@app.callback(
    Output('my-output', 'children'),
    Input('my-date-picker-single', 'date'),
    Input('my-input-day', 'value')
)
def update_graph(date_value, val):
    rate  = yc.svensson_rate(days = val,date = pd.Timestamp(date_value))
    return round(rate,2)

if __name__ == '__main__':
    app.run_server(debug = True, port =6969)
