# stalcker


## start
docker run --name data-stalker -p 8888:8888 -d public.ecr.aws/r0i2o0f6/data-stalker

and then
http://127.0.0.1:8888/

## install docker
sudo apt install -y docker.io
sudo usermod -aG docker $USER



	geometry 	citizen_id
0 	LINESTRING (116.33245 40.00335, 116.33252 40.0... 	910
1 	LINESTRING (116.32638 39.97474, 116.32763 39.9... 	594
2 	LINESTRING (116.29953 39.98654, 116.29949 39.9... 	590
3 	LINESTRING (116.26708 39.90544, 116.26708 39.9... 	964
4 	LINESTRING (116.32755 40.07588, 116.32756 40.0... 	977
... 	... 	...
980 	LINESTRING (116.32168 40.00097, 116.32504 39.9... 	309
981 	LINESTRING (116.30518 39.96661, 116.30516 39.9... 	544
982 	LINESTRING (116.32758 39.97777, 116.32772 39.9... 	252
983 	LINESTRING (116.33092 39.97522, 116.32492 39.9... 	344
984 	LINESTRING (116.44951 39.98682, 116.44964 39.9... 	125

985 rows × 2 columns


from ipyleaflet import Map, GeoData, basemaps
from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

m = Map(basemap=basemaps.Esri.WorldImagery, center = (40, 116.4), zoom =1)
#m = Map( center = (39, 116), zoom =3)
print(round(F(19)))
gdfnew = gdf[gdf.citizen_id == round(F(19))]

beijing_citizens = GeoData(geo_dataframe = gdfnew,
                   style={'color': 'red', 'opacity':4, 'weight':4, 'dashArray':'2', 'fillOpacity':0.6},
                   name = 'beijing_citizens')

m.add_layer(beijing_citizens)

display(m)

