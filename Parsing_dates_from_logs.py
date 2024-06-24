"""
INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
"""

from datetime import datetime,timedelta

start_Date=datetime.strptime("2014-07-03T23:27:51",'%Y-%m-%dT%H:%M:%S')
end_Date=datetime.strptime("2014-07-03T23:31:22",'%Y-%m-%dT%H:%M:%S')

print(((end_Date-start_Date).total_seconds())/60)
