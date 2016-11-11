##############################################################
#   Playing with JSON data in Python using requests and pandas
#   Author: Jacob Fowles
#   Date:   11-10-16
#   Notes:
#   1)  Data are courtesy of www.fantasyfootballnerd.com
#   2)  Set your working directory
##############################################################

# import modules
import os
import pandas as pd
import requests
import dateutil

# set working folder
os.chdir('/home/jacob/PycharmProjects/python_JSON')

# import JSON file into a pandas dataframe
nfl_games = pd.read_json('games.json', orient='columns')

# or just open it from the url directly
url = 'http://www.fantasyfootballnerd.com/service/schedule/json/test/'
r = requests.get(url)
#if this worked, we will see <Response [200]>
print(r)

# create a dataframe from the request
nfl_games = pd.DataFrame(r.json())

# view the first 5 rows of the dataframe
nfl_games.head

# convert strings to separate JSON objects based on column name
schedule = pd.read_json( (nfl_games['Schedule']).to_json(), orient='index')

# look at the first few rows of the new dataframe
schedule.head()

## Do some clever things, using functions from the imported and pre-canned modules##

# how many games are there this season?
len(schedule)

# tabulate the number of games by network
network_counts = schedule['tvStation'].value_counts()
network_counts

# list Denver's home schedule
milehigh = schedule[schedule['homeTeam'] == 'DEN']
milehigh = milehigh.sort_values(by='gameWeek')
milehigh

# convert string gameDate to actual date
schedule['gameDate'] = schedule['gameDate'].apply(dateutil.parser.parse, dayfirst=True)

# write the schedule dataframe to a csv file
schedule.to_csv('schedule.csv', sep=',')
