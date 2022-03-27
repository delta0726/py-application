# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : Examples
# Theme       : Graph in Tab
# Update Date : 2022/3/28
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/examples/graphs-in-tabs/
# ******************************************************************************


# ＜概要＞
# - レイアウトの画面構成をタブで管理する


# ＜参考＞
# Tabs - Components
# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tabs/


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\example\graph_in_tab.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリ起動


# 0 準備 ------------------------------------------------------------------------------------------

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html

# インスタンス生成
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



# 1 レイアウトの作成 ---------------------------------------------------------------------------------

# ＜ポイント＞
# - タブはネストさせることができる


app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.H1("Dynamically rendered tab content"),
        html.Hr(),
        dbc.Button(
            "Regenerate graphs",
            color="primary",
            id="button",
            className="mb-3",
        ),
        dbc.Tabs(
            [
                dbc.Tab(label="Scatter", tab_id="scatter"),
                dbc.Tab(label="Histograms", tab_id="histogram"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
        html.Div(id="tab-content", className="p-4"),
    ]
)


# 2 コールバックの作成 -----------------------------------------------------------------------

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"),
     Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab and data is not None:
        if active_tab == "scatter":
            return dcc.Graph(figure=data["scatter"])
        elif active_tab == "histogram":
            return dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
                    dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
                ]
            )
    return "No tab selected"


@app.callback(Output("store", "data"), [Input("button", "n_clicks")])
def generate_graphs(n):
    """
    This callback generates three simple graphs from random data.
    """
    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}

    # simulate expensive graph generation process
    time.sleep(2)

    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )
    hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
    hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])

    # save figures in a dictionary for sending to the dcc.Store
    return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2}


# 3 アプリ起動 ----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
