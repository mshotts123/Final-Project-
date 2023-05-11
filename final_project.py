import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'Table (3).csv', sep=',')
df=df[['GeoFips','GeoName','2021']]

import plotly.express as px
df = df.astype({'GeoFips' : 'str'})
print (df.info())
fips_abbr = {"53000": 'WA', "10000": 'DE', "11000": 'DC', "55000": 'WI', "54000": 'WV', "15000": 'HI', "12000": 'FL', "56000": 'WY', "72000": 'PR', "34000": 'NJ', "35000": 'NM', "48000": 'TX', "22000": 'LA', "37000": 'NC', "38000": 'ND', "31000": 'NE', "47000": 'TN', "36000": 'NY', "42000": 'PA', "2000": 'AK', "32000": 'NV', "33000": 'NH', "51000": 'VA', "8000": 'CO', "6000": 'CA', "1000": 'AL', "5000": 'AR', "50000": 'VT', "17000": 'IL', "13000": 'GA', "18000": 'IN', "19000": 'IA', "25000": 'MA', "4000": 'AZ', "16000": 'ID', "9000": 'CT', "23000": 'ME', "24000": 'MD', "40000": 'OK', "39000": 'OH', "49000": 'UT', "29000": 'MO', "27000": 'MN', "26000": 'MI', "44000": 'RI', "20000": 'KS', "30000": 'MT', "28000": 'MS', "45000": 'SC', "21000": 'KY', "41000": 'OR', "46000": 'SD'}
df["state_abbr"] = df["GeoFips"].map (fips_abbr)
print (df)
fig = px.choropleth(df,
                    locations='state_abbr', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='2021',
                    color_continuous_scale="Purples", 
                    #need to figure out how to set scale from 0 to 120,000,000
                    )
#colorbar ticks
cbar = plt.colorbar(ticks=[0, 120000000])

fig.update_layout(
      title_text = '2021 Inflow of Earnings by State',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45, 
         )
fig.show()