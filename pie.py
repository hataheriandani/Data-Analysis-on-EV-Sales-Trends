import pandas as pd
import lightningchart as lc
from lightningchart import Themes

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'electric-car-sales-share.csv'
data = pd.read_csv(file_path)

# Preparing data for the pie chart
data_grouped = data.groupby('Entity')['Share of new cars that are electric'].mean().reset_index()

regions = data_grouped['Entity']
sales_share = data_grouped['Share of new cars that are electric']

# Create the pie chart
chart = lc.PieChart(theme=Themes.White, title='Average Electric Car Sales Share by Region')

# Add slices to the pie chart
for region, share in zip(regions, sales_share):
    chart.add_slice(name=region, value=share)

# Open the chart
chart.open()