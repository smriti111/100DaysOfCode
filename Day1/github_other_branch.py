import requests as re
from datetime import date,datetime,timedelta 
import argparse
import json

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("username")
parser.add_argument("reponame")

# parse the arguments
args = parser.parse_args()

user = args.username
repo = args.reponame

url_branch = 'https://api.github.com/repos/{}/{}/branches'
data = re.get(url_branch.format(user,repo)).json() #'Rishabh1803','100DaysOfCode'

# fetching the latest commited branch
url_latest_branch = data[0]['commit']['url']
data = re.get(url_latest_branch).json()

# fetching latest commit date
latest_commit_date = data['commit']['committer']['date'][:10]
latest_commit_date_list = [int(i) for i in latest_commit_date.split('-')]
print(latest_commit_date_list[0], latest_commit_date_list[1], latest_commit_date_list[2])