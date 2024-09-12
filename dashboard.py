import pandas as pd
import lightningchart as lc

# Load dataset
file_path = 'IEA_Global_EV_Data_2024.csv'
data = pd.read_csv(file_path)

# Set license key
lc.set_license('my_license_key')

years = ['2018', '2019', '2020', '2021', '2022', '2023']
# List of regions and powertrains to handle
regions = ['China', 'Europe', 'USA', 'Rest of the world']
powertrains = ['BEV', 'PHEV']
# Create dashboard with 1 row and 4 columns (one for each region)
dashboard = lc.Dashboard(
    columns=4,
    rows=1,
    theme=lc.Themes.White
)
# Function to add a stacked bar chart for each region
def add_region_sales_to_dashboard(region, column_index, years):
    # Initialize dictionaries to store sales for each powertrain
    region_data = {pt: {year: 0 for year in years} for pt in powertrains}
    
    # Filter data for the region
    for powertrain in powertrains:
        filtered_data = data[(data['region'] == region) & 
                             (data['powertrain'] == powertrain) & 
                             (data['mode'] == 'Cars') & 
                             (data['year'].isin([int(year) for year in years]))]
        
        # Fill in sales data
        for index, row in filtered_data.iterrows():
            year = str(row['year'])
            region_data[powertrain][year] = row['value']

    # Prepare bar chart data for BEV and PHEV
    bar_data = []
    for powertrain in powertrains:
        values = [region_data[powertrain][year] for year in years]
        bar_data.append({'subCategory': f'{powertrain}', 'values': values})
    
    # Add bar chart for sales
    bar_chart = dashboard.BarChart(
        column_index=column_index,
        row_index=0,
    )
    bar_chart.set_data_stacked(
        years,
        bar_data
    )
    bar_chart.set_value_label_display_mode('hidden')
    bar_chart.set_title(f'Sales in {region}')

# Add each region's data to the dashboard
for i, region in enumerate(regions):
    add_region_sales_to_dashboard(region, i, years)

# Open the dashboard
dashboard.open()