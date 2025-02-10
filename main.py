from frontend.app import create_dash_app
from frontend.time_series import create_time_series_layout, register_time_series_callbacks

if __name__ == "__main__":
    app, ds, new_lat, new_lon = create_dash_app()

    # Add time-series layout
    app.layout.children.append(create_time_series_layout())

    # Register callbacks for time-series graph
    register_time_series_callbacks(app, ds)

    app.run_server(debug=True)
