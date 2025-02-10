import numpy as np
from scipy.interpolate import griddata

# Applies bilinear interpolation to convert a 6 arcminute (~0.1°) grid to a 1° grid.

def bilinear_interpolation(lat_values, lon_values, temp_values):
    unique_lat = np.unique(lat_values)
    unique_lon = np.unique(lon_values)

    if len(unique_lat) < 3 or len(unique_lon) < 3:
        raise ValueError("Not enough unique lat/lon points for interpolation. Check input data!")

    # Create new lat/lon grids using one degree per setp
    new_lat = np.linspace(-90, 90, 181)  
    new_lon = np.linspace(-180, 180, 361)  
    new_lat_grid, new_lon_grid = np.meshgrid(new_lat, new_lon, indexing="ij")


    # Ensure the original lat/lon grids are correctly meshed
    old_lon_grid, old_lat_grid = np.meshgrid(lon_values, lat_values, indexing="xy")  

    # Flatten 
    old_lat = old_lat_grid.ravel()
    old_lon = old_lon_grid.ravel()
    old_temp = temp_values.ravel()

    valid_points = ~np.isnan(old_temp)  # Mask out NaN values

    # Perform bilinear interpolation using Scipy
    new_temp = griddata(
        points=np.array([old_lat[valid_points], old_lon[valid_points]]).T,
        values=old_temp[valid_points],
        xi=(new_lat_grid, new_lon_grid),
        method="linear"
    )

    return new_lat, new_lon, new_temp
