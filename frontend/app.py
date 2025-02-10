from dash import Dash, dcc, html
import plotly.graph_objects as go
from src.data_loader import load_temperature_data
from src.interpolation import bilinear_interpolation
import numpy as np

def create_heatmap():
    """
    Load the temperature data, apply bilinear interpolation, and return the heatmap figure.
    """
    lat_range = (-90, 90)
    lon_range = (-180, 180)
    ds, _, lat_values, lon_values, temp_values = load_temperature_data(lat_range, lon_range)
    new_lat, new_lon, new_temp = bilinear_interpolation(lat_values, lon_values, temp_values)

    if len(new_lon.shape) == 1 and len(new_lat.shape) == 1:
        new_lon, new_lat = np.meshgrid(new_lon, new_lat)

    # Create heatmap figure
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
        title="Global Temperature Distribution (1970, 1° Grid)",
        width=1800,
        height=800
    )

    return fig, ds, new_lat, new_lon

def create_dash_app():
    app = Dash(__name__)

    # Create heatmap
    heatmap_fig, ds, new_lat, new_lon = create_heatmap()

    app.layout = html.Div(
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "width": "100vw"
        },
        children=[
            html.H1("Temperature Viewer"),
            dcc.Graph(
                id="temperature-map",
                figure=heatmap_fig,
                style={"maxWidth": "90vw", "maxHeight": "90vh"}
            )
        ]
    )

    return app, ds, new_lat, new_lon
