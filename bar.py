import pandas as pd
import lightningchart as lc
from lightningchart import Themes, Color

lc.set_license('my_license_key')

file_path = '/bev-share-new-ev.csv'
data = pd.read_csv(file_path)

years = data['Year'].astype(str)
bev_share = data['Battery-electric as a share of electric cars sold']
chart = lc.BarChart(theme=Themes.White, title='BEV Share of New EVs')
chart.set_sorting('alphabetical')
bar_data = [{'category': year, 'value': bev_share_value} for year, bev_share_value in zip(years, bev_share)]
chart.set_data(bar_data)
chart.add_textbox('Year', x=50, y=10) 
chart.add_textbox('BEV Share (%)', x=5, y=50) 
chart.open()
