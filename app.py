## write a template for plotly-dash app for displaying a 3d surface with dimensions that can be changed by the user and a slider for changing the angle of the surface
## import libraries
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly.graph_objs as go
#import numpy as np
#from dash.dependencies import Input, Output
#
## create a dash app
#app = dash.Dash()
#
## populare the 
#
## create a function for creating a 3d surface figure
#def create_3d_surface(x, y, z, angle):
#    return go.Figure(data=
#        [
#        go.Surface(x=x, y=y, z=z, colorscale='Viridis', showscale=False, opacity=0.8,
#            contours=dict(
#                x=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True)), 
#                y=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True)), 
#                z=dict(show=True, highlight=True, highlightcolor='red', project=dict(z=True))), 
#                lighting=dict(ambient=0.95, diffuse=0.99, fresnel=0.01, specular=0.01, roughness=0.01, facenormalsepsilon=1e-6, vertexnormalsepsilon=1e-12), 
#                lightposition=dict(x=100, y=200, z=0), 
#                lightdirection=dict(x=0, y=0, z=1), 
#                lightangle=angle, lightcolor='white', lighttype='cone', lightattenuation=2, opacity=0.8)
#        ]
#    )
#
## run the app
#if __name__ == '__main__':
#    app.run_server()
