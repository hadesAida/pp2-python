from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date 5 days ago:", new_date.strftime('%Y-%m-%d'))


from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", today.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))


from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("With microseconds:", current_datetime)
print("Without microseconds:", datetime_without_microseconds)

from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)  
date2 = datetime(2024, 2, 15, 14, 30, 0)  

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference_in_seconds)
