from dash import dcc, html, Output, Input
import plotly.express as px

def create_time_series_layout():
    """
    Returns the layout for the time-series graph, including sliders and unit toggle.
    """
    return html.Div(
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "width": "100vw"
        },
        children=[
            html.H1("Time-Series Temperature Viewer"),
            
            # Latitude slider
            html.Div([
                html.Label("Select Latitude:", style={"fontSize": "18px", "marginBottom": "10px"}),
                dcc.Slider(
                    id="lat-slider",
                    min=-90,
                    max=90,
                    step=1,
                    value=0,
                    marks={i: str(i) for i in range(-90, 91, 10)},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], style={"width": "80%", "margin": "20px"}),

            # Longitude slidr
            html.Div([
                html.Label("Select Longitude:", style={"fontSize": "18px", "marginBottom": "10px"}),
                dcc.Slider(
                    id="lon-slider",
                    min=-180,
                    max=180,
                    step=1,
                    value=0,
                    marks={i: str(i) for i in range(-180, 181, 20)},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], style={"width": "80%", "margin": "20px"}),

            # Temperature unit toggle
            html.Div([
                html.Label("Select Temperature Unit:", style={"fontSize": "18px", "marginBottom": "10px"}),
                dcc.RadioItems(
                    id="temp-unit",
                    options=[
                        {"label": "Kelvin (K)", "value": "K"},
                        {"label": "Celsius (°C)", "value": "C"}
                    ],
                    value="K",
                    inline=True,
                    style={"fontSize": "16px"}
                )
            ], style={"margin": "20px"}),

            # Time-series graph
            dcc.Graph(id="temp-graph", style={"width": "90%"})
        ]
    )

def register_time_series_callbacks(app, ds):
    """
    Registers the callback function to update the time-series graph.
    """
    @app.callback(
        Output("temp-graph", "figure"),
        [Input("lat-slider", "value"),
         Input("lon-slider", "value"),
         Input("temp-unit", "value")]
    )
    def update_timeseries(selected_lat, selected_lon, temp_unit):
        temp_series = ds["tas"].sel(lat=selected_lat, lon=selected_lon, method="nearest").to_pandas()

        # Convert to Celsius if selected
        if temp_unit == "C":
            temp_series = temp_series - 273.15
            y_label = "Temperature (°C)"
        else:
            y_label = "Temperature (K)"

        fig = px.line(temp_series, x=temp_series.index, y=temp_series.values,
                      title=f"Temperature Over Time at Selected Location (1970)",
                      labels={"x": "Time (Date in 1970)", "y": y_label})

        return fig
