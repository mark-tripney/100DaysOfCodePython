from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
print(type(t))

# We can examine the days in this timedelta object
print(t.days)

# What if we want to know how many seconds are in the object?
print(t.seconds)
# This returns 36,000... but that's not right! 36,000 seconds is just the 10
# hours part. Why? timedelta can only go up to a certain amount of time, like
# a stopwatch. Seconds can only go up to a maximum of one day.

eta = timedelta(hours=14)
now = datetime.today()

print((eta + now).strftime("%H:%M %p"))

print(eta + now)
