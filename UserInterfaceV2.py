import dash
from collections import OrderedDict
from Solutions import Solution
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go
import Titration
import plotly.plotly as py
from dash.dependencies import Input, Output, State
from DataBase import DataBase

reader = DataBase();
Acids = reader.ReadJSONFile("WeakSolutionNames")
WeakAcidDictionary = []
for x in Acids:
    WeakAcidDictionary.append({'label': x, 'value': x})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#Section For getting a data for drop down menu
reader = DataBase()
WeakAcidTitrant = WeakAcidDictionary
WeakAcidAnalyte = WeakAcidDictionary
#initialize graph


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
data = OrderedDict(
    [
        ("Titrant", ["Not Selected"]),
        ("Analyte", ["Not Selected"]),
        ("Titrant Volume", [0]),
        ("Analyte Volume", [0]),
        ("PH", [0]),
    ]
)
df = pd.DataFrame(data)


app.layout = html.Div(
    [
        #ROW 1
        html.Div(
            [
                html.H3("Acid Base Graphing Calculator",className = "12 columns top-fixed", style = {"color":"white","margin": 20,"width":"100vh"})
            ]
            , className = "row", style = {"backgroundColor" :"#629fd1"}),

        #ROW 2
        html.Div(
            [
            html.Div(
                [
                html.Label("Titrant (Solution Added)"),
                dcc.Dropdown(id ="titrant-solution-state", options= WeakAcidDictionary)
                ],className = "six columns"),
                html.Div(

                    [
                     html.Label("Analyte (Base Solution)"),
                     dcc.Dropdown(id ="analyte-solution-state", options=WeakAcidDictionary)
                    ],className="six columns")
                 ], className= "row",style = {"textAlign": "center"}),

        #ROW 3
        html.Div(
            [
            #6 Columns
            html.Div(
                [
                    html.Label("Titrant Molarity"),
                    dcc.Input(id ="titrant-molarity-state", value='', type='number',placeholder='Enter a value...'),
                ], className="six columns"),
                 #6 Columns
            html.Div(
                [
                    html.Label("Analyte Molarity"),
                    dcc.Input(id ="analyte-molarity-state", value='', type='number',placeholder='Enter a value...'),
                 ],className="six columns")
            ], className="row",style = {"textAlign": "center"}),
        #Row 4
        html.Div(
             [
            #6 Columns
             html.Div(
                 [
                      html.Label("Titrant Volume (ml)"),
                      dcc.Input(id ="titrant-volume-state", value='', type='number',placeholder='Enter a value...'),
                 ],className="six columns"),
            #6 Columns
             html.Div(
                 [
                 html.Label("Analyte Volume (ml)"),
                 dcc.Input(id ="analyte-volume-state" ,value='', type='number',placeholder='Enter a value...' ),
                 ],className="six columns")
             ], className="row",style = {"textAlign": "center"}),
        #Row 5
        html.Div(
        [
            #12 Columns
            html.Div(
            [
                 html.Label("Press When Ready To Begin"),
                 html.Button('Begin', id='submit-button', n_clicks = 0,style = {'width':'100%'}),
            ],className = "twelve columns" , style = {"leftMargin" : [10,100,10,100]})
        ], className="row", style = {"textAlign": "center"}),
        #Row 6
        html.Div(
            [
                dcc.Graph( id = 'output-state'),
                html.Div(
                     [
                      html.H3("Titration Number Summary", style = {"textAlign" : "center"}),
                     ])
            ], className="row"),
        #Row 7
        html.Div(
            [
                dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df.columns])
            ], className = "row", id = "summary-output")
    ], style = {"margin" : [10,100,10,100]})

@app.callback(
    dash.dependencies.Output('titrant-solution-state', 'options'),
    [dash.dependencies.Input('analyte-solution-state', 'value')])

def update_TitrantList(value):
    Name = reader.ReadJSONFile("WeakSolutionNames")
    KA = reader.ReadJSONFile("KAValues")
    WeakAcidTitrant = WeakAcidDictionary
    if not(value == None):
        print("Change")
        WeakAcidTitrant[Name.index(value)] = ({'label': value, 'value': value, 'disabled' :True})
        # Test Case If selected solution is weak
        if(KA[(Name.index(value))] > 1*(10**-14) and KA[(Name.index(value))] < 1):
            for x in range(0, WeakAcidTitrant.__len__()):
                if(KA[x] > 1*(10**-14) and KA[x] < 1):
                    WeakAcidTitrant[x] = ( {'label': Name[x], 'value': Name[x],'disabled': True})  # Which by default, has disabled set to False

            if(KA[(Name.index(value))] > 1*(10**-7) and KA[(Name.index(value))] < 1):
                for x in range(0, WeakAcidTitrant.__len__()):
                    if (KA[x] >= 1):
                        WeakAcidTitrant[x] = ({'label': Name[x], 'value': Name[x], 'disabled': True})  # Which by default, has disabled set to False
            else:
                for x in range(0, WeakAcidTitrant.__len__()):
                    if (KA[x] <= 1*(10**-14)):
                        WeakAcidTitrant[x] = ({'label': Name[x], 'value': Name[x],'disabled': True})  # Which by default, has disabled set to False
        if(KA[(Name.index(value))] <= 1*(10**-14) or KA[(Name.index(value))] <= 1):
             if(KA[(Name.index(value))] <= 1*(10**-14)):
                 for x in range(0, WeakAcidTitrant.__len__()):
                     if (KA[x] <= 1 * (10 ** -7)):
                         WeakAcidTitrant[x] = ({'label': Name[x], 'value': Name[x],
                                                   'disabled': True})  # Which by default, has disabled set to False
        if(KA[(Name.index(value))] >= 1):
            for x in range(0, WeakAcidTitrant.__len__()):
                if (KA[x] >= (1 * (10 ** -7))):
                    WeakAcidTitrant[x] = ({'label': Name[x], 'value': Name[x],
                                              'disabled': True})  # Which by default, has disabled set to False
        return WeakAcidTitrant
    if(value == None):

        for x in range(0,WeakAcidTitrant.__len__()):
            WeakAcidTitrant[x] = ({'label': Name[x], 'value': Name[x]}) #Which by default, has disabled set to False
        print("None")
        return WeakAcidTitrant

    return WeakAcidDictionary
@app.callback(
    dash.dependencies.Output('analyte-solution-state', 'options'),
    [dash.dependencies.Input('titrant-solution-state', 'value')])

def update_AnalyteList(value):
    Name = reader.ReadJSONFile("WeakSolutionNames")
    KA = reader.ReadJSONFile("KAValues")
    WeakAcidAnalyte = WeakAcidDictionary
    if not(value == None):
        print("Change")
        WeakAcidAnalyte[Name.index(value)] = ({'label': value, 'value': value, 'disabled' :True})
        # Test Case If selected solution is weak
        if(KA[(Name.index(value))] > 1*(10**-14) and KA[(Name.index(value))] < 1):
            for x in range(0, WeakAcidAnalyte.__len__()):
                if(KA[x] > 1*(10**-14) and KA[x] < 1):
                    WeakAcidAnalyte[x] = ( {'label': Name[x], 'value': Name[x],'disabled': True})  # Which by default, has disabled set to False

            if(KA[(Name.index(value))] > 1*(10**-7) and KA[(Name.index(value))] < 1):
                for x in range(0, WeakAcidAnalyte.__len__()):
                    if (KA[x] >= 1):
                        WeakAcidAnalyte[x] = ({'label': Name[x], 'value': Name[x], 'disabled': True})  # Which by default, has disabled set to False
            else:
                for x in range(0, WeakAcidAnalyte.__len__()):
                    if (KA[x] <= 1*(10**-14)):
                        WeakAcidAnalyte[x] = ({'label': Name[x], 'value': Name[x],'disabled': True})  # Which by default, has disabled set to False
        if(KA[(Name.index(value))] <= 1*(10**-14) or KA[(Name.index(value))] <= 1):
             if(KA[(Name.index(value))] <= 1*(10**-14)):
                 for x in range(0, WeakAcidAnalyte.__len__()):
                     if (KA[x] <= 1 * (10 ** -7)):
                         WeakAcidAnalyte[x] = ({'label': Name[x], 'value': Name[x],
                                                   'disabled': True})  # Which by default, has disabled set to False
             if(KA[(Name.index(value))] >= 1):
                 for x in range(0, WeakAcidAnalyte.__len__()):
                     if (KA[x] >= (1 * (10 ** -7))):
                         WeakAcidAnalyte[x] = ({'label': Name[x], 'value': Name[x],
                                                  'disabled': True})  # Which by default, has disabled set to False
        return WeakAcidAnalyte
    if(value == None):

        for x in range(0,WeakAcidAnalyte.__len__()):
            WeakAcidAnalyte[x] = ({'label': Name[x], 'value': Name[x]}) #Which by default, has disabled set to False
        print("None")
        return WeakAcidAnalyte

    return WeakAcidDictionary


@app.callback(Output('summary-output','children'),[Input('submit-button','n_clicks')],[State('analyte-volume-state','value'),
                                                                          State('titrant-volume-state', 'value'),
                                                                          State('analyte-molarity-state', 'value'),
                                                                          State('titrant-molarity-state', 'value'),
                                                                          State('titrant-solution-state', 'value'),
                                                                          State('analyte-solution-state', 'value')])
def update_summary_output(n_clicks,analytevolume,titrantvolume,analytemolarity,titrantmolarity,titrantsolution,analytesolution):
    KA = reader.ReadJSONFile("KAValues")
    Name = reader.ReadJSONFile("WeakSolutionNames")
    if not (analytesolution == None or titrantsolution == None):
        AnalyteKA = KA[Name.index(analytesolution)]
        TitrantKA = KA[Name.index(titrantsolution)]
        newPh = Titration.DeterminePH(Solution("Blah",TitrantKA,titrantmolarity,titrantvolume),Solution("Blah",AnalyteKA,analytemolarity,analytevolume))

        summary = OrderedDict(
        [
            ("Titrant", [titrantsolution]),
            ("Analyte", [analytesolution]),
            ("Titrant Volume", [titrantvolume]),
            ("Analyte Volume", [analytevolume]),
            ("PH", [newPh]),
        ]
        )
        df = pd.DataFrame(summary)
        return dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns])

@app.callback(Output('output-state','figure'),[Input('submit-button','n_clicks')],
                                                                            [State('analyte-volume-state','value'),
                                                                          State('titrant-volume-state', 'value'),
                                                                          State('analyte-molarity-state', 'value'),
                                                                          State('titrant-molarity-state', 'value'),
                                                                          State('titrant-solution-state', 'value'),
                                                                          State('analyte-solution-state', 'value')])
def update_output(n_clicks,analytevolume,titrantvolume,analytemolarity,titrantmolarity,titrantsolution,analytesolution):
    KA = reader.ReadJSONFile("KAValues")
    Name = reader.ReadJSONFile("WeakSolutionNames")
    if not(analytesolution == None or titrantsolution == None):
        AnalyteKA = KA[Name.index(analytesolution)]
        TitrantKA = KA[Name.index(titrantsolution)]
        listx,listy = Titration.getCoordinatePairs(titrantsolution,
                                                   TitrantKA,
                                                   titrantmolarity
                                                   ,titrantvolume
                                                   ,analytesolution
                                                   ,AnalyteKA
                                                   ,analytemolarity
                                                   ,analytevolume)

        return {'data' :[go.Scatter(
            x = listy,
            y = listx,
            #mode = 'markers',
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
                  yaxis = {
                              'title': 'PH',
                              'type': 'linear'
                          },
                          margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
                                   hovermode = 'closest'
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
    app.run_server(debug=True,port = 8080)