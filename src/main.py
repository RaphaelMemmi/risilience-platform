import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_temperature_data
from interpolation import bilinear_interpolation

# Define global latitude and longitude range
lat_range = (-90, 90)  
lon_range = (-180, 180)  

# Load dataset and extract relevant data
ds, small_grid, lat_values, lon_values, temp_values = load_temperature_data(lat_range, lon_range)

# Apply bilinear interpolation to convert the dataset to a 1° grid
new_lat, new_lon, new_temp = bilinear_interpolation(lat_values, lon_values, temp_values)

# Ensure correct longitude and latitude shapes
if len(new_lon.shape) == 1 and len(new_lat.shape) == 1:
    new_lon, new_lat = np.meshgrid(new_lon, new_lat)

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot temperature data
mesh = ax.pcolormesh(new_lon, new_lat, new_temp, cmap="coolwarm", shading='auto')

# Add colorbar
fig.colorbar(mesh, ax=ax, label="Temperature (K)")

# Set axis labels and title
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Global Temperature After Bilinear Interpolation (1° Grid)")

plt.show()
