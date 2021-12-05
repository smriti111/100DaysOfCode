import subprocess
import sqlite3
import os
from datetime import date, timedelta
name_list=['Rishabh','Smriti','Mohit','Muskaan']
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
db_path=os.path.join(BASE_DIR, "test.db")
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

for i in cursor.execute("SELECT * FROM Commit_Tracker "):
   print(i)
print("<---------------------Completed--------------------------------->")

cursor.execute('''UPDATE Commit_Tracker
                  SET Day = Day+1''')
 


username_list=['Rishabh1803','Smriti111']
repo_list = ['100DaysOfCode','100-Days-of-Code']
url='https://api.github.com/repos/{}/{}/commits'
status1,output1 = subprocess.getstatusoutput('github_commit_daily_report.py Smriti111 100-Days-of-Code')
output1 = [int(i) for i in output1.split()]
smr_latest_commit = date(output1[0],output1[1],output1[2])
print(smr_latest_commit)

status2,output2 = subprocess.getstatusoutput('github_other_branch.py Rishabh1803 100DaysOfCode')
output2 = [int(i) for i in output2.split()]
ris_latest_commit = date(output2[0],output2[1],output2[2]) 
print(ris_latest_commit)


if smr_latest_commit == date.today():
    cursor.execute('''UPDATE Commit_Tracker
                  SET Points = Points+1
                  Where Name = 'Smriti' ''')


if ris_latest_commit == date.today():
    cursor.execute('''UPDATE Commit_Tracker
                  SET Points = Points+1
                  Where Name = 'Rishabh' ''')  
 
connection.commit()
print ("{:<10} {:<15} {:<15} {:<10}".format('Name','Days_Commited','Days_Missed','Points'))
for row in cursor.execute("SELECT * FROM Commit_Tracker "):
    print("{:<10} {:<15} {:<15} {:<10}".format(row[0],row[1],row[2]-row[1],row[1]))

connection.close()