# Climate Temperature Viewer

A web application that displays global temperature data. This was very fun to make!

## Features

- **Global Heatmap**: Displays daily near-surface temperature (in Kelvin) on a 1° grid for the year 1970.
- **Time-Series Graph**: Shows temperature variation over 1970 for a selected latitude/longitude.
- **Unit Toggle**: Switch between Kelvin and Celsius.
- **Responsive UI**: Built with Dash for a user-friendly experience.

## Requirements

- **Docker** and **Docker Compose** (recommended for running the application)
- **Data File** - add the "tas...nc" data file into your local folder. The file was too big to push on here

## Project Structure

```
.
├── main.py                # Entry point for the Dash app
├── frontend/
│   ├── app.py             # Heatmap creation and Dash setup
│   ├── time_series.py     # Time-series layout & callbacks for Dash
├── src/
│   ├── data_loader.py     # Data loading and preprocessing
│   ├── interpolation.py   # Bilinear interpolation logic
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # This file
```

## Getting Started 

1. **Build and Run with Docker Compose**:
   ```sh
   docker-compose up --build
   ```

2. **Access the Application**:
   Open [http://localhost:8050](http://localhost:8050) in your browser.


## Extensions

Some ideas for a future version could include:
- **Map Overlay**: OVerlay a Map of the world ontop of the HeatMap to better view each country and border 
- **Degree Changer**: A slider which changes the degrees of the grid. This could help view how the size of the grid changes the HeatMap.


