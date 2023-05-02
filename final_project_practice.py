import pandas as pd 

df = pd.read_csv(r'state_market_tracker.tsv000', sep='\t')
df=df[['period_begin','state','state_code','property_type','median_sale_price']]
df=df[(df['period_begin']=='2022-01-01') & (df['property_type']=='Single Family Residential')] 
df.rename({'median_sale_price':'Median Sales Price ($)'},axis=1, inplace=True)


import plotly.express as px
fig = px.choropleth(df,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Median Sales Price ($)',
                    color_continuous_scale="Viridis_r", 
                    
                    )
fig.show()

