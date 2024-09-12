import pandas as pd
import lightningchart as lc
from lightningchart import Themes
import time

# Set the license key
my_license_key = 'P001-ZgAiXcls82XucLjGo1pNDBmgknE/FgAGIi2wGJsKgHy4pMYuLCxrxf4UXnNH-MEQCIE7WrKAMcHSuauBhMtQTwX3JPNSQPhQvdGJFy5GoAArCAiBsiHovJHY6pyh59fLdvj+QT5ld5MbewJXf7NsivQvsUw=='
lc.set_license(my_license_key)

# Load the dataset, skipping the first few rows of metadata
file_path = 'C:/Users/Taheri/Desktop/darsi/m8.5/workplacement/project 7/global-electric-car-stock-2013-2023.csv'
data = pd.read_csv(file_path, skiprows=3, sep=';')

# Extracting the 'Year' and the global electric car stock
years = data.iloc[:, 0].astype(int).tolist()
global_stock = data.iloc[:, 1:].sum(axis=1).astype(float).tolist()
# Create the XY chart with a real-time simulation
chart = lc.ChartXY(theme=Themes.White, title='Global Electric Car Stock (2013-2023)')
series = chart.add_line_series()
# Initialize an empty data list for simulating real-time updates
x_values = []
y_values = []
# Set axis titles
x_axis = chart.get_default_x_axis()
x_axis.set_title("Year")
x_axis.set_decimal_precision(0)
y_axis = chart.get_default_y_axis()
y_axis.set_title("Number of Electric Cars (in millions)")
# Open the chart in real-time mode
chart.open(live=True)
# Simulate real-time data update
for i in range(len(years)):
    x_values.append(int(years[i]))
    y_values.append(float(global_stock[i]))
    series.set_samples(x_values, y_values)
    time.sleep(1)
