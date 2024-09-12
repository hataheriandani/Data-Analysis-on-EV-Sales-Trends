import pandas as pd
import lightningchart as lc
from lightningchart import Color, Themes

# Set the license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'electric-car-sales-share.csv'
data = pd.read_csv(file_path)

# Function to create a world map chart
def create_world_map_chart(data, year):
    # Filter data for the given year
    data_year = data[data['Year'] == year]
    data_year = data_year[['Code', 'Share of new cars that are electric']].rename(columns={'Code': 'ISO_A3', 'Share of new cars that are electric': 'value'})

    # Create the MapChart for World
    chart = lc.MapChart(map_type='World', theme=lc.Themes.White)

    # Set sales share data
    chart.invalidate_region_values(data_year.to_dict(orient='records'))
    # Set title with year
    chart.set_title(f"Electric Car Sales Share - Year {year} - World")
    chart.set_palette_colors(
        steps=[
            {'value': 0, 'color': Color('#f7fbff')},
            {'value': 0.2, 'color': Color('#FFFF99')},
            {'value': 0.5, 'color': Color('#FFD700')},
            {'value': 0.7, 'color': Color('#FFCC99')},
            {'value': 0.9, 'color': Color('#FF8C00')},
            {'value': 1, 'color': Color('#FF9999')},
            {'value': 1.5, 'color': Color('#FF0000')},
            {'value': 2, 'color': Color('#238b45')},
            {'value': 25, 'color': Color('#41ae76')},
            {'value': 30, 'color': Color('#66c2a4')}
        ],
        look_up_property='value',
        percentage_values=True
    )
    # Enable hover highlighting
    chart.set_highlight_on_hover(enabled=True)
    legend = chart.add_legend(horizontal=True, title=f"Electric Car Sales Share - Year: {year}", data=chart)
    legend.set_font_size(10)
    chart.open(live=True)
    return chart

create_world_map_chart(data, 2023)
