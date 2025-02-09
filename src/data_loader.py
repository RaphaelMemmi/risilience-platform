import xarray as xr
import numpy as np

# Load temperature data from a NetCDF file and extract a subset based on latitude and longitude ranges

def load_temperature_data(lat_range, lon_range):
    # Load dataset
    ds = xr.open_dataset("tas_day_EC-Earth3_historical_r101i1p1f1_gr_19700101-19701231.nc")

    # Convert longitudes from [0, 360] to [-180, 180] and ensure correct ordering
    ds = ds.assign_coords(lon=(("lon",), np.where(ds["lon"] > 180, ds["lon"] - 360, ds["lon"])))
    ds = ds.sortby(ds.lon)

    small_grid = ds["tas"].sel(lat=slice(*lat_range), lon=slice(*lon_range))

    # Select only the first time step to prevent shape mismatch issues
    small_grid = small_grid.isel(time=0)

    return ds, small_grid, small_grid["lat"].values, small_grid["lon"].values, small_grid.values
