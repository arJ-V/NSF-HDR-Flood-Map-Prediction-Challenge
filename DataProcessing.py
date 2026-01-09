import netCDF4 as nc
import pandas as pd
import numpy as np
import xarray as xr
import re
import os
from google.colab import drive
from pathlib import Path
import tqdm
from tqdm import tqdm

# Open the NetCDF file
file_path = '/content/dt_ena_19930101_vDT2021.nc'
dataset = nc.Dataset(file_path, 'r')

# Explore the dataset structure
print(dataset)               # Basic information about the dataset
print(dataset.variables)     # List of variables in the file

# Extract spatial and temporal metadata
lat_min = dataset.geospatial_lat_min  # Minimum latitude
lat_max = dataset.geospatial_lat_max  # Maximum latitude
lon_min = dataset.geospatial_lon_min  # Minimum longitude
lon_max = dataset.geospatial_lon_max  # Maximum longitude

# Extract time coverage
time_start = dataset.time_coverage_start  # Start date
time_end = dataset.time_coverage_end      # End date

# Display the extracted information
print(f"Spatial Coverage:\nLatitude: {lat_min}° to {lat_max}°\nLongitude: {lon_min}° to {lon_max}°")
print(f"Date Range:\nStart Date: {time_start}\nEnd Date: {time_end}")

# Close the dataset
dataset.close()

# Open the NetCDF file
file_path = '/content/dt_ena_19930101_vDT2021.nc'  # Replace with your file path
dataset = nc.Dataset(file_path, 'r')  # Open in read mode

# Extract dimensions (e.g., time, latitude, longitude)
time = dataset.variables['time'][:].data  # Time dimension
lat = dataset.variables['latitude'][:].data  # Latitude dimension
lon = dataset.variables['longitude'][:].data  # Longitude dimension

# Create a meshgrid of latitude and longitude (for 3D data flattening)
lon_grid, lat_grid = np.meshgrid(lon, lat)

# Initialize a dictionary to store extracted data
data_dict = {
    'latitude': lat_grid.flatten(),
    'longitude': lon_grid.flatten(),
}

ds = xr.open_dataset('/content/dt_ena_19930101_vDT2021.nc')

# Inspect the dataset
print(ds.head)


# Accessing 'sla' (Sea Level Anomaly)
sla_data = ds['sla'].values
latitude = ds['latitude'].values
longitude = ds['longitude'].values
time = ds['time'].values

print("Shape of SLA:", sla_data.shape)

# Use regex to extract the date (assuming the date is always in the format YYYYMMDD)
# def extract_date(filename):
#   match = re.search(r'(\d{8})', filename)

#   if match:
#       date_str = match.group(1)  # Extracted date as string
#       #print(f"Extracted date: {date_str}")

#       # Optionally, convert to a datetime object
#       from datetime import datetime
#       date = datetime.strptime(date_str, '%Y%m%d')
#       return date

drive.mount('/content/drive')

folder_path = '/content/drive/MyDrive/Flood_prediction/iharp_training_dataset/Copernicus_ENA_training_data'

# Path to your directory
#folder_path = Path('/content/drive/myDrive/')  # Replace with the actual path

# List all files in the directory
files = os.listdir(folder_path)

type(files)
num_files = len(files)
num_files

range(num_files)

# Paths to the uploaded NetCDF files

# Atlantic City coordinates
atlantic_city_lat = 39.356667
atlantic_city_lon = -74.418053

# Initialize an empty list to store daily data
daily_data = []

num_files = len(files)
# Loop through each NetCDF file
for file_num in tqdm(range(num_files)):
    file = files[file_num]
    file_path = folder_path+'/'+file
    # Open the NetCDF file
    ds = xr.open_dataset(file_path)

    # Extract relevant variables and filter for Atlantic City's location
    daily_sla = ds['sla'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_adt = ds['adt'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_ugosa = ds['ugosa'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_vgosa = ds['vgosa'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_err_sla = ds['err_sla'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_err_ugosa = ds['err_ugosa'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_err_vgosa = ds['err_vgosa'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_flag_ice = ds['flag_ice'].sel(
        latitude=atlantic_city_lat, longitude=atlantic_city_lon, method='nearest'
    ).values
    daily_time = pd.to_datetime(ds['time'].values[0])

    # Append the date and SLA value to the daily data list
    daily_data.append({'date': daily_time, 'sla': daily_sla, 'adt': daily_adt, 'ugosa': daily_ugosa, 'vgosa': daily_vgosa, 'err_sla': daily_err_sla, 'err_ugosa': daily_err_ugosa, 'err_vgosa': daily_err_vgosa, 'flag_ice': daily_flag_ice})
    ds.close()

# Convert the daily data into a DataFrame
nc_data = pd.DataFrame(daily_data)

# Inspect the aggregated NetCDF data
nc_data.head()


nc_data.to_csv('nc_data.csv')

folder_path2 = '/content/drive/MyDrive/Flood prediction/iharp_training_dataset/Training_Anomalies'


# Flatten the SLA values
nc_data['sla'] = nc_data['sla'].apply(lambda x: x[0] if isinstance(x, (list, np.ndarray)) else x)

# Reload the Atlantic City anomaly data
atlantic_city_csv_path = folder_path2 + '/'+ 'Atlantic_City_1993_2013_training_data.csv'
atlantic_city_data = pd.read_csv(atlantic_city_csv_path)

# Convert dates to datetime format for merging
atlantic_city_data['t'] = pd.to_datetime(atlantic_city_data['t'])
nc_data['date'] = pd.to_datetime(nc_data['date'])

# Merge the NetCDF data with the CSV data
merged_data = pd.merge(atlantic_city_data, nc_data, left_on='t', right_on='date', how='inner')

# Inspect the merged dataset
merged_data.head()

merged_data.to_csv('merged_data.csv')

