import pandas as pd
df = pd.read_csv(r'Table (3).csv', sep='\t')
df=df[['GeoFips','GeoName','2021']]

import plotly.express as px
fig = px.choropleth(df,
                    locations='GeoFips', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='State Gross Inflow of Earnings ($)',
                    color_continuous_scale="Viridis_r", 
                    #need to figure out how to set scale from 0 to 120,000,000
                    
                    )
fig.show()