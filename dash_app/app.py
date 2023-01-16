# write a template for plotly-dash app for displaying a 3d surface with dimensions that can be changed by the user and a slider for changing the angle of the surface
# import libraries
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# create a dash app
app = dash.Dash()

# load tensor data from file
tensore_equazione_sigma = np.load('./tensore_equazione_sigma_book.npy')

# create a function for creating a 3d surface figure
def create_3d_surface(x, y, z):
    fig =  go.Figure(data=
        [
        go.Surface(x=x, y=y, z=z, colorscale='Viridis', showscale=False, opacity=0.8,
            contours=dict(
                    x=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True)), 
                    y=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True)), 
                    z=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True))
                    ), 
                )
        ]
    )
    fig.update_layout(
        autosize=False,
        width=800, height=800,
        margin=dict(l=65, r=50, b=65, t=90),
        uirevision='constant',
        scene = dict(
            xaxis_title='Disistima ricevuta',
            yaxis_title='Rifiuto effettivo',
            zaxis_title='Sigma'))
    return fig

# create a layout for the app with sliders for changing the z value passed to the function
app.layout = html.Div([
    html.H1('Sigma equation'),
    # display the two divs next to each other
    dcc.Tab(
        html.Div([
            dcc.Graph(id='3d-surface', figure=create_3d_surface(np.arange(0, 1.1, 0.1), np.arange(0, 1.1, 0.1), tensore_equazione_sigma[0,0,0,:,:])),
        ], style={'width': '60%', 'display': 'inline-block'}),
        label='Equazione sigma',),
    # display the sliders next to the figure
    dcc.Tab(
        html.Div([
                html.H3('Cecità'),
                dcc.Slider(
                    id='cecita-slider',
                    min=0,
                    max=100,
                    step=10,
                    value=0,
                    marks={i: '{}%'.format(i) for i in range(0, 110, 10)}
                ),
                html.H3('Complessità'),
                dcc.Slider(
                    id='complessita-slider',
                    min=0,
                    max=100,
                    step=10,
                    value=0,
                    marks={i: '{}%'.format(i) for i in range(0, 110, 10)}
                ),
                html.H3('Disistima espressa'),
                dcc.Slider(
                    id='disistima_espressa-slider',
                    min=0,
                    max=100,
                    step=10,
                    value=0,
                    marks={i: '{}%'.format(i) for i in range(0, 110, 10)}
                ),
        ], style={'width': '35%','padding': '0px 0px 0px 0px','display': 'inline-block','vertical-align': 'top',
}),
        label='Parametri',),
])

# create a callback for updating the figure
@app.callback(
    Output('3d-surface', 'figure'),
    [Input('cecita-slider', 'value'), Input('complessita-slider', 'value'), Input('disistima_espressa-slider', 'value')]
)
def update_figure(cecita, complessita, disistima_espressa):
    # divide all values by 10 to get the values between 0 and 1
    cecita = int(cecita/10)
    complessita =  int(complessita/10)
    disistima_espressa =  int(disistima_espressa/10)
    # get the current value of the angles of the surface
    return create_3d_surface(np.arange(0, 1.1, 0.1), np.arange(0, 1.1, 0.1), tensore_equazione_sigma[cecita,complessita,disistima_espressa,:,:])

# run the app
if __name__ == '__main__':
    app.run_server()
