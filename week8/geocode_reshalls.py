##############################################################
#   Playing with JSON data in Python using requests and pandas
#   Author: Jacob Fowles
#   Date:   11-10-16
#   Notes:
#   1)  This uses Google Maps API in a loop. Don't be a jerk.
##############################################################

#import modules
import os
import pandas as pd
import requests
import dateutil


#input list of addresses to geocode from CSV file, format for urls
halls = pd.read_csv('data\reshalls.csv')
halls['street'] = halls['street'].str.replace(' ','+')
halls.zip = halls.zip.astype(str)
halls['full_addr'] = halls['street'] + "," + halls['city'] + "," + halls['state'] + "," + halls['zip']

#create new variables
halls['g_address'] = ''
halls['g_latlon'] = ''

#loop over urls, add to dataset
for row in halls['full_addr']:
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + row
    print(url)
    #grab info from google
    r = requests.get(url)
    # if this worked, we will see <Response [200]>
    print(r)
    # create a data frame from from json data
    r_df = pd.DataFrame(r.json())
    r_df.head(1)
    df = r_df['results'].apply(pd.Series)
    df.head(1)
    #pull out the address
    df_fadd = df['formatted_address'].apply(pd.Series)
    #write it to the row of the dataframe
    
    #pull out the GIS coordinates
    df_geo = df['geometry'].apply(pd.Series)
    df_loc = df_geo['location'].apply(pd.Series)
    df_loc.head(1)
    #write it to the row of the dataframe
    





