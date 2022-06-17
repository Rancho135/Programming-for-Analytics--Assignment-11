#****************************************************************
#Name:Goodnews Agbadu
#Student Number: A00238219

#ANA1001 Assignment 11
#****************************************************************



'''Pick two places and download temperature data and time for both create a dictionary using the following format temps = {“time”:[],“place1”:[],”place2”:[]} and save this data to a json file called temps.json. In order to match up, you will need to write the time, then the two temps, and repeat. Log enough data that you are able to do an analysis over time (Minimum 5 days of data). Read the JSON file and create a graph with labels showing both sets of temperature data (y-axis) and time series (x-axis), make sure to include labels for the chart, x and y axes.'''

import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.read_csv("temp_dataAfrica.csv") #remember to use your directory
#view the dataset

#using this data let us select the temperatures of two cities
lagos = df[df['City'] == 'Lagos']
kampala = df[df['City'] ==  'Kampala']

#extract the year and AvgTemperature column
lagos = lagos[['Year','AvgTemperature']]
kampala = kampala[['Year','AvgTemperature']]

#find the average temperature for each year
lagos = lagos.groupby('Year')['AvgTemperature'].mean().to_frame().reset_index()
kampala = kampala.groupby('Year')['AvgTemperature'].mean().to_frame().reset_index()

#merge the two dataframes
df = pd.merge(lagos,kampala,on='Year')

#creating a dictionary
temps = {"time":list(df['Year']),
        "place1":list(df['AvgTemperature_x']),
        "place2":list(df["AvgTemperature_y"])}

# Serializing json to help in writing the file
json_temps = json.dumps(temps, indent = 4)

#writing the json file
with open("temps.json", "w") as f:
    f.write(json_temps)
    
#opening the json file
with open("temps.json", "r") as of:
    temp = json.load(of)

#plotting the data
plt.figure(figsize = (10,6))
plt.plot(temp['time'],temp['place1']) #plot for place1
plt.plot(temp['time'],temp['place2']) #plot for place2
plt.title("Annual average temperature of place1 and place2 (2000 - 2020)") #add the title
plt.xlabel("Time") #label the x - axis
plt.ylabel("Average Temperature") #label the  y - axis
plt.legend(["place1","place2"]) #add the legend to show which line represents which place
plt.savefig("temp.jpg", bbox_inches = "tight")


'''Generate a visualization using synthetically generated data of your choice (not weather related , could be csv or json).'''
# taking the data
pd = pd.read_csv('pd.csv')
#print(pd['Stress'])

# creating histogran
fig, axer = plt.subplots(figsize =(10, 7))
axer.hist(pd['Stress'])
 

plt.title('My Stress Level histogram (Scale of 1-5)')
plt.xlabel('Stress')
plt.ylabel('Number of Times Stressed at Each Scale')
# Show plot
plt.savefig("3.jpg", bbox_inches = "tight")

'''Use Earthquake.csv (attached) and create a Scattergeo visualization using Plotly, which shows the magnitudes of all the earthquakes in the csv file. Use the fields latitude and longitude from within the csv to plot the locations.'''
import csv
filename = "eq.csv"

with open(filename) as file_object:
  reader = csv.reader(file_object)
  header_row = next(reader)
#print(header_row)

#Printing the Headers and Their Positions
#for i, col_header in enumerate(header_row):
  #print(i,col_header)

#Extracting Mag, lons and lats 
  mags, lons, lats = [], [], []

  for row in reader:
    mag = float(row[4])
    mags.append(mag)
    lon = float(row[2])
    lons.append(lon)
    lat = float(row[1])
    lats.append(lat)
    
print(mags[0:20])
print(lons[0:5])
print(lats[0:5])

#Building a world map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#Maping the earthquakes
data = [{
  "type": 'scattergeo',
  "lat": lats, 
  "lon": lons,
  "marker":{"size":[5*mag for mag in mags],"color":mags, "colorscale":'Viridis',"reversescale":True, "colorbar":{'title': 'magnitude'}}
}]
my_layout = Layout(title = "Earthquakes around the World")

figure = {'data': data, 'layout': my_layout}
#Saving file in a HTML
offline.plot(figure, filename = 'eqmap.html')


'''Use Earthquake.csv (attached) and create a histogram(like we studied last week) of all the depths in the csv file.'''

# importing libaries
import matplotlib.pyplot as plt
import pandas as pd
# taking the data
df = pd.read_csv('eq.csv')
#print(df['depth'])

# creating histogran
fig, axer = plt.subplots(figsize =(10, 7))
axer.hist(df['depth'])
 
plt.title('Earthquake Depths histogram')
plt.xlabel('Depths')
plt.ylabel('Total Depths')
# Show plot
plt.savefig("temp2.jpg", bbox_inches = "tight")