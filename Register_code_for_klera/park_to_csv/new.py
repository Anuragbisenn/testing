# Importing the required libraries
from turtle import title
import xml.etree.ElementTree as Xet
import pandas as pd
import pyarrow

cols = ["id", "title", "description", "location", "lng", "lat", "userId"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('Samplexml100.xml')
root = xmlparse.getroot()
for i in root:

	id = i.findtext("id")
	title = i.findtext("title")
	description = i.findtext("description")
	location = i.findtext("location")
	lng = i.findtext("lng")
	lat = i.findtext("lat")
	userId= i.findtext("userId")




	rows.append({"id": id,"title": title,"description":description ,"location":location, "lng": lng,"lat":lat,"userId":userId})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
df.to_parquet( 'df.parquet.gzip',compression='gzip')
data = pd.read_parquet('df.parquet.gzip',engine='pyarrow')
print(data)