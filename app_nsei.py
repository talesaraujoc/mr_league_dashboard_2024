from dash import dash, html, dcc, Output, Input, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


import plotly as plt
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_ag_grid as dag


# Servidor
app = dash.Dash(__name__)

server = app.server

# DataFrame =================

from globals import *

# Pré-layout ================


# Layout    =================
app.layout = html.Div([

])


# Callbacks =================



# Servidor  =================
if __name__ == '__main__':
    app.run_server(debug=False)