# Data Analysis on EV Sales Trends with LightningChart Python
## Introduction
In recent years, electric vehicle (EV) sales have surged across the globe, reflecting a significant shift in the automotive industry towards more sustainable transportation solutions. The economic outlook of EV sales has been driven by a variety of factors, including technological advancements, environmental concerns, governmental policies, and consumer demand for eco-friendly vehicles. Countries like the United States, China, and many European nations have seen exponential growth in EV adoption, and this trend is expected to continue.
As the global automotive market evolves, EV sales are influenced by a range of dynamic factors including advancements in battery technology, fluctuations in oil prices, and regulatory changes aimed at reducing carbon emissions. Additionally, the expansion of charging infrastructure and the introduction of new EV models are contributing to increased consumer confidence and adoption.
Analyzing EV sales trends is crucial for understanding the market's future. By examining the data, we can gain insights into which regions are leading EV adoption, what factors are influencing growth, and how consumer behavior is changing. Through data analysis, it's possible to predict future EV sales trends, helping both manufacturers and consumers make informed decisions. This proactive approach can guide strategic planning, policy-making, and investment decisions, ultimately supporting the global transition to cleaner, more sustainable transportation.
## LightningChart Python
#### Overview of LightningChart Python
In this project, we will use LightningChart Python, a high-performance charting library, to visualize and analyze EV sales data. By leveraging Python's data analysis capabilities, along with tools like NumPy and LightningChart, we aim to create comprehensive visualizations that highlight EV sales trends over time. This analysis will offer valuable insights into how EV sales trends are shaping the future of the automotive industry and impacting electric vehicle adoption rates.
### Features and Chart Types to be Used in the Project
In this project, we will utilize various chart types available in LightningChart to visualize EV Sales Trends data:
- **Line Chart:** Ideal for showing trends over time, the line chart will help us visualize the progression of EV sales across different years and identify patterns or fluctuations.
- **Bar Chart:** Useful for comparing EV sales data across different countries or regions, the bar chart provides a clear view of the relative performance of each area.
- **Stacked Bar Chart:** This chart will enable us to break down EV sales data into different segments, such as vehicle types or market segments, to understand the composition and contribution of each segment over time.
- **Map Chart:** By using a map chart, we can visualize geographical distribution and adoption rates of EVs across different regions, providing spatial context to the sales trends.
- **Pie Chart:** The pie chart will illustrate the proportion of EV sales relative to total car sales in different regions or globally, helping to highlight the share of electric vehicles in the overall market.

### Performance Characteristics
LightningChart is known for its exceptional performance, handling large datasets with ease and providing smooth interactions and animations.

### Setting Up Python Environment
#### Installing Python and Necessary Libraries
To get started, you need to have Python installed on your system. You can download Python from the official website. Additionally, you will need to install the following libraries:

```bash
pip install pandas lightningchart
```
#### Overview of Libraries Used
- **Pandas:** For data manipulation and analysis.
- **LightningChart:** For creating high-performance visualizations.

#### Setting Up Your Development Environment
Set up your development environment by installing the required libraries and organizing your project files, including the EV Sales Trends data files.

#### How to Load the Data Files
You can load the EV Sales Trends data files using Pandas. Here’s an example:
```bash
file_path = '/bev-share-new-ev.csv'
data = pd.read_csv(file_path)
```
### Visualizing Data with LightningChart
#### Introduction to LightningChart for Python
LightningChart provides a range of visualization options, making it ideal for exploring and presenting complex datasets like EV Sales Trends changes.

### Creating the Charts
Here are the codes and brief analyses for the various charts used in this project.
- **1- Line chart**
Sales of electric cars started from a low base but are growing quickly in many markets.
```bash
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

```
![Line](/images/l1.gif)

```bash
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

```
Sales of electric cars started from a low base but are growing quickly in many markets.
Globally, around 1-in-4 new cars sold were electric in 2023. This share was over 90% in Norway, and in China, it was almost 40%.
In the chart below, you can explore these trends across the world.


![lines](/images/l2.gif)

```bash
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

```
![lineS_live](/images/l3.gif)

- **2- Bar chart**
In 2010 and 2011, the electric vehicle market was still in its early stages, and most sales were dominated by fully battery-electric vehicles (BEVs). At that time, plug-in hybrid electric vehicles (PHEVs) were relatively new and underdeveloped, leading to a higher share of BEVs in the overall electric vehicle market. In the following years, as the market evolved, automakers introduced more PHEV models, which led to a decline in the share of BEVs. Many consumers began favoring hybrid options, causing the market to become more balanced between BEVs and PHEVs from 2012 onwards.

```bash
years = data['Year'].astype(str)
bev_share = data['Battery-electric as a share of electric cars sold']
chart = lc.BarChart(theme=Themes.White, title='BEV Share of New EVs')
chart.set_sorting('alphabetical')
bar_data = [{'category': year, 'value': bev_share_value} for year, bev_share_value in zip(years, bev_share)]
chart.set_data(bar_data)
chart.add_textbox('Year', x=50, y=10) 
chart.add_textbox('BEV Share (%)', x=5, y=50) 
chart.open()

```
![bar](/images/bar1.png)

- **3- Stacked bar chart**
The stacked bar chart illustrates the sales data of Battery Electric Vehicles (BEV) and Plug-in Hybrid Electric Vehicles (PHEV) across various regions, including China, Europe, the USA, and the Rest of the World, from 2013 to 2023. This chart effectively visualizes how different regions and powertrain types (BEV vs. PHEV) have contributed to the growth of the global electric vehicle market during this period.
```bash
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
```
![stacked](/images/stacked.png)

- **4- Map chart**
In 2023, the global adoption of electric cars varies significantly. High adoption rates are seen in some regions with strong incentives and infrastructure. In contrast, many regions show moderate to low adoption, reflecting barriers such as cost and limited infrastructure. Overall, while there's a notable trend toward electric vehicles, substantial disparities exist globally.
```bash
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

```
![map](/images/map.png)
- **5- Pie chart**
The pie chart displays the average percentage of electric vehicle sales across various countries and regions worldwide. It is evident from the chart that Norway places significant importance on the infrastructure for electric vehicle production. Iceland, Sweden, and Finland are the next leading countries in this area.
```bash
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
```
![pie](/images/pie.png)

## Conclusion
This project has provided an analysis of electric vehicle (EV) sales trends using LightningChart Python. Through the examination of recent economic outlooks and influencing factors, we have gained insights into the dynamics of EV sales in various markets. Data analysis has proven to be a valuable tool in predicting future EV sales trends and understanding their implications for the automotive industry.
By leveraging LightningChart Python, we have effectively visualized complex datasets, highlighting the impact of current EV sales trends on adoption rates. The use of advanced chart types and performance characteristics of LightningChart Python has enhanced our ability to present data clearly and informatively.
The benefits of using LightningChart Python are evident in the improved accuracy and efficiency of data visualization, which facilitates better decision-making and forecasting. Overall, this project underscores the importance of data analysis and visualization in understanding and predicting EV market trends, contributing valuable insights to the ongoing evolution of the automotive industry.
### References
- International Energy Agency: [IEA](https://www.iea.org/reports/global-ev-outlook-2024/trends-in-electric-cars)
- Python Official Documentation: [Python](https://www.python.org/)
- LightningChart Documentation: [LightningChart](https://lightningchart.com/python-charts/docs/charts/)
- Our World in Data : [ourworldindata](https://ourworldindata.org/electric-car-sales)