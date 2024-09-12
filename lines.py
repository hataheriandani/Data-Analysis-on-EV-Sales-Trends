import pandas as pd
import lightningchart as lc
from lightningchart import Themes
import time

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'electric-car-sales-share.csv'
data = pd.read_csv(file_path)
print(data)

# Specify the regions of interest
regions_of_interest = ['World', 'Norway', 'United Kingdom', 'European Union (27)', 'China', 'United States']

# Filter the dataset for the specified regions and sort by year
filtered_data = data[data['Entity'].isin(regions_of_interest)].sort_values(by='Year')

# Function to create live line chart for a region
def create_live_chart(region_name):
    # Filter data for the specific region
    region_data = filtered_data[filtered_data['Entity'] == region_name]
    years = region_data['Year'].astype(int).tolist()
    sales_share = region_data['Share of new cars that are electric'].astype(float).tolist()
    
    # Create a chart for each region
    chart = lc.ChartXY(theme=Themes.White)
    chart.set_title(f"{region_name} Electric Car Sales Share")
    series = chart.add_line_series()

    # Initialize empty lists for live simulation
    x_values = []
    y_values = []

    # Set axis titles
    chart.get_default_x_axis().set_title("Year")
    chart.get_default_y_axis().set_title("Sales Share (%)")

    # Simulate live updates
    for i in range(len(years)):
        # Append the new data point
        x_values.append(int(years[i]))  # Ensure values are Python integers
        y_values.append(float(sales_share[i]))  # Ensure values are Python floats

        # Update the chart with the new data
        series.set_samples(x_values, y_values)

        # Pause for a moment to simulate real-time update
        time.sleep(0)  # Update every second (adjust time interval as needed)

    # Open the chart in the browser
    chart.open(live=True)

# Create live charts for each region in separate browser windows/tabs
create_live_chart('World')
create_live_chart('Norway')
create_live_chart('United Kingdom')
create_live_chart('European Union (27)')
create_live_chart('China')
create_live_chart('United States')
