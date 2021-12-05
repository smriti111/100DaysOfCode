import argparse
import requests as re
from datetime import date,datetime,timedelta

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("username")
parser.add_argument("reponame")

# parse the arguments
args = parser.parse_args()

user = args.username
repo = args.reponame
 

url_commit = ' https://api.github.com/repos/{}/{}/commits'  # .format('username','repo_name')
data = re.get(url_commit.format(user,repo)).json() #Smriti111 vue_weather_app

# fetching date form the json response dictionary
latest_commit_date = data[0]['commit']['author']['date'][:10]

latest_commit_date_list = [int(i) for i in latest_commit_date.split('-')]

# converting raw date to date object
print(latest_commit_date_list[0],latest_commit_date_list[1],latest_commit_date_list[2])
