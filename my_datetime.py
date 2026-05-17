import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)

weekday = now.strftime("%a")
print(weekday)
