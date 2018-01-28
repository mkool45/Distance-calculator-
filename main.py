import pandas as pd #import pandas library
from geopy.distance import vincenty
#import vincenty formula used to to calculate the distance between two points on the surface of a spheroid from geopy library
import config #import config file
import json #import json library since input is in json format

def get_distance(lat1, lon1):
	#This function takes latitude and longitude and returns haversine distance between that point and office coordinates
	office_coordinates = (config.office_latitude, config.office_longitude)
	customer_coordinates = (lat1, lon1)
	distance = float(str(vincenty(office_coordinates, customer_coordinates)).split()[0])
	return distance

df = pd.read_json(config.input_file, lines=True) #dataframe is used because it contains two dimensional labelled data structures

df['distance'] = df[['latitude','longitude']].apply(lambda x: get_distance(x[0],x[1]), axis=1)

df = df[(df.distance < config.defined_range)] #condition to get user id's within 100 Kms
df = df.sort_values(['user_id']) #sorting the user id's
cols = ['user_id', 'name', 'latitude', 'longitude', 'distance']
df = df[cols] #creation of coloumns containing details of users
x = (df['user_id'].values.tolist()) #series of sorted user id's
print("The sorted list of user id's within a distance of 100Kms from the GPS co-ordinates 53.339428 and -6.257664 is")
for letter in x:
    print(letter) # this prints a list containing sorted user ids
df.to_csv(config.output_file, index = False)
#Creates a excel file containing details of sorted users including their names, co-ordinates and distance from the office
