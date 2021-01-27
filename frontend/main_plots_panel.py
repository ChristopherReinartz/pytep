import pandas as pd

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from app import app
from backend.siminterface.siminterface import MainPlotInterface

mpp_interface = MainPlotInterface.dummy_interface()

main_plots_panel = html.Div(
    [
        dbc.Row(
            [
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p1'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p1")],
                    className="w-50 h-100",
                    id="main-plot-one",
                    style={"background-color": "blue", "border": "solid"},
                ),
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p2'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p2")],
                    className="w-50 h-100",
                    id="main-plot-two",
                    style={"background-color": "blue", "border": "solid"}
                )
            ],
            className="h-25",
        ),
        dbc.Row(
            [
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p3'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p3")],
                    className="w-50 h-100",
                    id="main-plot-three",
                    style={"background-color": "blue", "border": "solid"}
                ),
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p4'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p4")],
                    className="w-50 h-100",
                    id="main-plot-four",
                    style={"background-color": "blue", "border": "solid"}
                )
            ],
            className="h-25",
        ),        dbc.Row(
            [
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p5'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p5")],
                    className="w-50 h-100",
                    id="main-plot-five",
                    style={"background-color": "blue", "border": "solid"}
                ),
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p6'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p6")],
                    className="w-50 h-100",
                    id="main-plot-six",
                    style={"background-color": "blue", "border": "solid"}
                )
            ],
            className="h-25",
        ),        dbc.Row(
            [
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p7'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p7")],
                    className="w-50 h-100",
                    id="main-plot-seven",
                    style={"background-color": "blue", "border": "solid"}
                ),
                dbc.Col([
                    dcc.Dropdown(options=[{'label': label, 'value': label} for label in mpp_interface.labels()],
                                 value=['time'],
                                 multi=False,
                                 clearable=False,
                                 id='dropdown_p8'),
                    dcc.Graph(figure={}, className="w-100 h-100", id="graph_p8")],
                    className="w-50 h-100",
                    id="main-plot-eight",
                    style={"background-color": "blue", "border": "solid"}
                )
            ],
            className="h-25",
        ),
    ],
    id="main-plots-panel",
    className="h-100 w-100",
)


@app.callback(
    Output(component_id='graph_p1', component_property='figure'),
    Input(component_id='dropdown_p1', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)

@app.callback(
    Output(component_id='graph_p2', component_property='figure'),
    Input(component_id='dropdown_p2', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)

@app.callback(
    Output(component_id='graph_p3', component_property='figure'),
    Input(component_id='dropdown_p3', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)

@app.callback(
    Output(component_id='graph_p4', component_property='figure'),
    Input(component_id='dropdown_p4', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)


@app.callback(
    Output(component_id='graph_p5', component_property='figure'),
    Input(component_id='dropdown_p5', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)


@app.callback(
    Output(component_id='graph_p6', component_property='figure'),
    Input(component_id='dropdown_p6', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)


@app.callback(
    Output(component_id='graph_p7', component_property='figure'),
    Input(component_id='dropdown_p7', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)


@app.callback(
    Output(component_id='graph_p8', component_property='figure'),
    Input(component_id='dropdown_p8', component_property='value')
)
def plot_on_p1(col_label):
    return scatter(col_label)


def scatter(col_label):
    data = mpp_interface.timed_var(col_label)
    fig = px.scatter(x=data['time'], y=data[col_label])
    fig.update_layout(xaxis_title='time',
                      yaxis_title=col_label)
    fig.update_layout(autosize=True)
    return fig