# %%
# Process
import pandas as pd
import numpy as np
import geopandas
import shapely.wkt
import folium
import mysql.connector
import json

# Set env
import os
os.environ["USE_PYGEOS"] = "0"
import contextily as cx

# %%
df = pd.read_csv('./POINT_20181024_1.csv')

# %%
# หัว
df.head()

# %%
# หาง
df.tail()

# %%
df.shape

# %%
df.info()

# %%
df.hist()

# %%
df.describe()

# %%
df['LATITUDE'].isnull()

# %%
df['LONGITUDE'].isnull()

# %%
# ลบแถวที่ latitude,longitude เป็น Nan
df = df.dropna(subset=['LATITUDE','LONGITUDE'],axis='rows')

# %%
# Check categories
df['CELL_STATUS'].value_counts()

# %%
# Get index of CELL_STATUS is warning
dfs = df[((df['CELL_STATUS'] != 'ACTIVE') & (df['CELL_STATUS'] != 'DEACTIVE'))]
dfs.head()

# %%
# find to set
df.loc[dfs.index,'CELL_STATUS'] = 'DEACTIVE'

# %%
# view after set
df.iloc[dfs.index]

# %%
# transform column geometry
df['geometry'] = df[['LATITUDE','LONGITUDE']].apply(lambda row: 'POINT (' + row['LATITUDE'].astype(str) + ' ' + row['LONGITUDE'].astype(str) + ')',axis=1)

# %%
df.head()

# %%
# convert dataframe to geo dataframe
locations = geopandas.GeoDataFrame(df, geometry=df['geometry'].apply(shapely.wkt.loads),crs='epsg:4326')

# %%
locations.shape

# %%
map_1 = folium.Map(zoom_start=15,control_scale = True,crs='epsg:4326')

# %%
# plot data
locations.explore()

# %%
# load geometry json จังหวัด เพชรบุรี
with open('./petchaburi.json','r',encoding='utf8') as f:
    province = json.load(f)
    f.close()

print(province)

# %%
# create polygon petchaburi
petchaburi = geopandas.GeoDataFrame.from_features(province['features'],crs=4326)

# %%
point_in_polygon = geopandas.sjoin(locations,petchaburi,op='within',how='inner')

# %%
location_within_petchaburi = locations.loc[point_in_polygon.index]

# %%
location_within_petchaburi.shape

# %%
location_within_petchaburi.explore()

# %%
# connection
conn = mysql.connector.connect(host="localhost",user="root",password="",database="final")

# %%
if conn.is_connected():
    print('Connected Successfully')
else:
    print('Failed to Connect') 

# %%
cursor = conn.cursor()

# %%
truncate_stmt = 'TRUNCATE TABLE location'
cursor.execute(truncate_stmt) 

# %%
for index in location_within_petchaburi.index:
    insert_stmt = 'INSERT INTO location (CELL_STATUS,LATITUDE,LONGITUDE) VALUES (%s,%s,%s)'
    val = (str(location_within_petchaburi.loc[index].CELL_STATUS),float(location_within_petchaburi.loc[index].LATITUDE),float(location_within_petchaburi.loc[index].LONGITUDE))
    cursor.execute(insert_stmt,val)
    conn.commit()

# %%
# write folder
if not os.path.exists('./logs'):
    os.makedirs('./logs')
    
# write stats
content = str('{ "stats_within": ' + str(location_within_petchaburi.shape[0]) + ', "stats_not_within": ' + str(locations.shape[0] - location_within_petchaburi.shape[0]) + ' }')
f = open('./logs/stats.json', 'wb')
f.write(bytes(content,encoding='utf8'))
f.close()

# %%
print('Done.')


