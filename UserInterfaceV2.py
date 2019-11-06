import dash
from collections import OrderedDict
from Solutions import Solution
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go
import Titration
from dash.dependencies import Input, Output, State
from DataBase import DataBase

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

reader = DataBase();

# Section For getting a data for drop down menu
solutions = reader.read_json_file("Solutions")
solution_name_list = []
for x in solutions:
    solution_name_list.append({'label': x.get("name"), 'value': x.get("name")});

# initialize graph
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# Default Output Table Values
data = OrderedDict(
    [
        ("Titrant", ["Not Selected"]),
        ("Analyte", ["Not Selected"]),
        ("Titrant Volume", [0]),
        ("Analyte Volume", [0]),
        ("PH", [0]),
    ]
)

# DOM Python Script
df = pd.DataFrame(data)
app.layout = html.Div(
    [
        # ROW 1
        html.Div(
            [
                html.H3("Acid Base Graphing Calculator", className="12 columns top-fixed",
                        style={"color": "white", "margin": 20, "width": "100vh"})
            ]
            , className="row", style={"backgroundColor": "#629fd1"}),

        # ROW 2
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Titrant (Solution Added)"),
                        dcc.Dropdown(id="titrant-solution-state", options=solution_name_list)
                    ], className="six columns"),
                html.Div(

                    [
                        html.Label("Analyte (Base Solution)"),
                        dcc.Dropdown(id="analyte-solution-state", options=solution_name_list)
                    ], className="six columns")
            ], className="row", style={"textAlign": "center"}),

        # ROW 3
        html.Div(
            [
                # 6 Columns
                html.Div(
                    [
                        html.Label("Titrant Molarity"),
                        dcc.Input(id="titrant-molarity-state", value='', type='number', placeholder='Enter a value...'),
                    ], className="six columns"),
                # 6 Columns
                html.Div(
                    [
                        html.Label("Analyte Molarity"),
                        dcc.Input(id="analyte-molarity-state", value='', type='number', placeholder='Enter a value...'),
                    ], className="six columns")
            ], className="row", style={"textAlign": "center"}),
        # Row 4
        html.Div(
            [
                # 6 Columns
                html.Div(
                    [
                        html.Label("Titrant Volume (ml)"),
                        dcc.Input(id="titrant-volume-state", value='', type='number', placeholder='Enter a value...'),
                    ], className="six columns"),
                # 6 Columns
                html.Div(
                    [
                        html.Label("Analyte Volume (ml)"),
                        dcc.Input(id="analyte-volume-state", value='', type='number', placeholder='Enter a value...'),
                    ], className="six columns")
            ], className="row", style={"textAlign": "center"}),
        # Row 5
        html.Div(
            [
                # 12 Columns
                html.Div(
                    [
                        html.Label("Press When Ready To Begin"),
                        html.Button('Begin', id='submit-button', n_clicks=0, style={'width': '100%'}),
                    ], className="twelve columns", style={"leftMargin": [10, 100, 10, 100]})
            ], className="row", style={"textAlign": "center"}),
        # Row 6
        html.Div(
            [
                dcc.Graph(id='output-state'),
                html.Div(
                    [
                        html.H3("Titration Number Summary", style={"textAlign": "center"}),
                    ])
            ], className="row"),
        # Row 7
        html.Div(
            [
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns])
            ], className="row", id="summary-output")
    ], style={"margin": [10, 100, 10, 100]})


def get_ka_values(analytesolution, titrantsolution):
    if not (analytesolution is None or titrantsolution is None):
        analyte_ka = []
        titrant_ka = []
        for solution in solutions:
            if solution.get("name") == analytesolution:
                analyte_ka = solution.get("Ka")
            elif solution.get("name") == titrantsolution:
                titrant_ka = solution.get("Ka")
    return analyte_ka, titrant_ka

# Event Call Backs

# Begin Titration Button Event
@app.callback(Output('summary-output', 'children'), [Input('submit-button', 'n_clicks')],
              [State('analyte-volume-state', 'value'),
               State('titrant-volume-state', 'value'),
               State('analyte-molarity-state', 'value'),
               State('titrant-molarity-state', 'value'),
               State('titrant-solution-state', 'value'),
               State('analyte-solution-state', 'value')])
def update_summary_output(n_clicks, analytevolume, titrantvolume, analytemolarity, titrantmolarity, titrantsolution,
                          analytesolution):
    if not (analytesolution is None or titrantsolution is None):
        analyte_ka, titrant_ka = get_ka_values(analytesolution, titrantsolution)

        for solution in solutions:
            if solution.get("name") == analytesolution:
                analyte_charge = solution.get("charge")
            elif solution.get("name") == titrantsolution:
                titrant_charge = solution.get("charge")

        new_ph = Titration.DeterminePH(Solution("titrant", titrant_ka, titrantmolarity, titrantvolume, titrant_charge),
                                       Solution("analyte", analyte_ka, analytemolarity, analytevolume, analyte_charge))

        # Updated summary information
        summary = OrderedDict(
            [
                ("Titrant", [titrantsolution]),
                ("Analyte", [analytesolution]),
                ("Titrant Volume", [titrantvolume]),
                ("Analyte Volume", [analytevolume]),
                ("PH", [new_ph]),
            ]
        )

        data_table = pd.DataFrame(summary)
        return dash_table.DataTable(
            data=data_table.to_dict('records'),
            columns=[{'id': d, 'name': d} for d in data_table.columns])

# Update graph of titration
@app.callback(Output('output-state', 'figure'), [Input('submit-button', 'n_clicks')],
              [State('analyte-volume-state', 'value'),
               State('titrant-volume-state', 'value'),
               State('analyte-molarity-state', 'value'),
               State('titrant-molarity-state', 'value'),
               State('titrant-solution-state', 'value'),
               State('analyte-solution-state', 'value')])
def update_output(n_clicks, analytevolume, titrantvolume, analytemolarity, titrantmolarity, titrantsolution,
                  analytesolution):
    if not(analytesolution is None or titrantsolution is None):
        analyte_ka, titrant_ka = get_ka_values(analytesolution, titrantsolution)

        for solution in solutions:
            if solution.get("name") == analytesolution:
                analyte_charge = solution.get("charge")
            elif solution.get("name") == titrantsolution:
                titrant_charge = solution.get("charge")

        liters_to_ml = .001  # Conversion Factor

        titrant = Solution(titrantsolution, titrant_ka, titrantmolarity, titrantvolume * liters_to_ml, titrant_charge)
        analyte = Solution(analytesolution, analyte_ka, analytemolarity, analytevolume * liters_to_ml, analyte_charge)

        list_y, list_x = Titration.getCoordinatePairs(titrant, analyte)

        return {'data': [go.Scatter(
            x= list_x,
            y= list_y,
            # mode = 'markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
            'layout': go.Layout(
                xaxis={
                    'title': 'Ml of Titrant',
                    'type': 'linear'
                },
                yaxis={
                    'title': 'PH',
                    'type': 'linear'
                },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                hovermode='closest'
            )
        }
    return {'data': [go.Scatter(
        x=[0],
        y=[0],
        # mode = 'markers',
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'}
        }
    )],
        'layout': go.Layout(
            xaxis={
                'title': 'Ml of Titrant',
                'type': 'linear'
            },
            yaxis={
                'title': 'PH',
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
