from dash import Dash, dcc, html
import plotly.graph_objects as go
from src.data_loader import load_temperature_data
from src.interpolation import bilinear_interpolation
import numpy as np

def create_dash_app():
    app = Dash(__name__)
    
    # Load the temperature data and interpolate it
    lat_range = (-90, 90)
    lon_range = (-180, 180)
    _, _, lat_values, lon_values, temp_values = load_temperature_data(lat_range, lon_range)
    new_lat, new_lon, new_temp = bilinear_interpolation(lat_values, lon_values, temp_values)
    
    if len(new_lon.shape) == 1 and len(new_lat.shape) == 1:
        new_lon, new_lat = np.meshgrid(new_lon, new_lat)

    # Create a figure for the plot
    fig = go.Figure()
    fig.add_trace(go.Heatmap(
        z=new_temp,
        x=new_lon[0],
        y=new_lat[:, 0],
        colorscale="thermal",
        colorbar={"title": "Temperature (K)"}
    ))

    fig.update_layout(
    xaxis_title="Longitude",
    yaxis_title="Latitude",
    title="Global Temperature After Bilinear Interpolation",
    width=1800,  
    height=800   
)

    app.layout = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "height": "100vh"  
    },
    children=[
        html.H1("Temperature Viewer"),
        dcc.Graph(
            id="temperature-map",
            figure=fig,
            style={
                "maxWidth": "90vw",  
                "maxHeight": "90vh" 
            }
        )
    ]
)

    
    return app
