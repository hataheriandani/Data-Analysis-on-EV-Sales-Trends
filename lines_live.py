import pandas as pd
import lightningchart as lc
import time

my_license_key = 'P001-ZgAiXcls82XucLjGo1pNDBmgknE/FgAGIi2wGJsKgHy4pMYuLCxrxf4UXnNH-MEQCIE7WrKAMcHSuauBhMtQTwX3JPNSQPhQvdGJFy5GoAArCAiBsiHovJHY6pyh59fLdvj+QT5ld5MbewJXf7NsivQvsUw=='
lc.set_license(my_license_key)

# Load the dataset
file_path = 'C:/Users/Taheri/Desktop/darsi/m8.5/workplacement/project 7/bev-share-new-ev.csv'
data = pd.read_csv(file_path)

# List of countries and regions to include in the chart, including Americas
entities = ['Norway', 'Finland', 'China', 'United Kingdom', 'United States', 'Japan']

# Create the chart
chart = lc.ChartXY(
    theme=lc.Themes.White,
    title='Share of new cars that are electric'
)

# Define colors for each entity
colors = [
    lc.Color(0, 0, 255),
    lc.Color(255, 165, 0), 
    lc.Color(255, 255, 0),
    lc.Color(0, 255, 0),
    lc.Color(255, 0, 0),
    lc.Color(0, 0, 0)
]

# Create a line series for each entity
line_series_dict = {}
for i, entity in enumerate(entities):
    line_series = chart.add_line_series()
    line_series.set_name(entity)
    line_series.set_line_color(colors[i])
    line_series.set_line_thickness(2)
    line_series_dict[entity] = line_series

# Customize x-axis
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')
x_axis.set_decimal_precision(0)

# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('Battery-electric as a share of electric cars sold (percentage)')

# Add a legend to the chart
chart.add_legend(
    horizontal=False,
    title='Regions',
    x=12 , y=42,
    data=chart
)

# Open the chart
chart.open(live=True)

# Add data points with a delay to simulate real-time drawing
for index, row in data.iterrows():
    if row['Entity'] in entities:
        year = row['Year']
        emission = row['Battery-electric as a share of electric cars sold']
        if pd.notna(year) and pd.notna(emission):
            emission_million = emission / 1e6  # Convert to million metric tons
            print(f"Adding data for {row['Entity']}: Year={year}, Emission={emission_million}")
            line_series_dict[row['Entity']].add(year, emission_million)
            time.sleep(0.1)  # 0.1 second delay between each data point

chart.close()
