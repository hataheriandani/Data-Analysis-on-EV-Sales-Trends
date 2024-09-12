import pandas as pd
import lightningchart as lc

# Load dataset
file_path = 'IEA_Global_EV_Data_2024.csv'
data = pd.read_csv(file_path)

# Set license key
lc.set_license('my_license_key')

years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# List of regions and powertrains to handle
regions = ['China', 'Europe', 'USA', 'Rest of the world']
powertrains = ['BEV', 'PHEV']

region_powertrain_data = {region: {pt: {year: 0 for year in years} for pt in powertrains} for region in regions}

for region in regions:
    for powertrain in powertrains:
        filtered_data = data[(data['region'] == region) & 
                             (data['powertrain'] == powertrain) & 
                             (data['mode'] == 'Cars') & 
                             (data['year'].isin([int(year) for year in years]))]
        
        # Debug: Print the filtered data for each region and powertrain
        print(f"Filtered {region} {powertrain} Data:", filtered_data)
        
        # Fill in the dictionary with available data
        for index, row in filtered_data.iterrows():
            year = str(row['year'])
            if year in region_powertrain_data[region][powertrain]:
                region_powertrain_data[region][powertrain][year] = row['value']

chart_data = []
for region in regions:
    for powertrain in powertrains:
        values = [region_powertrain_data[region][powertrain][year] for year in years]
        chart_data.append({'subCategory': f'{region} {powertrain}', 'values': values})


# Create a chart
chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.White,
    title='BEV and PHEV sales by Region (2013-2023)'
)
chart.set_sorting('disabled')
# Set stacked bar chart data
chart.set_data_stacked(
    years,
    chart_data
)

# Customize chart
chart.set_value_label_display_mode('hidden')
chart.add_legend(x=15,y=45).add(chart)

# Open the chart
chart.open()