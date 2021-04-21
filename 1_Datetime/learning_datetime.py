# Imports
from datetime import datetime
from datetime import date

# The full datetime object
right_now = datetime.today()
print(f"Datetime: {right_now}")
print(f"Type: {type(right_now)}")

# More specific - get today's date
today_date = date.today()
print(f"\nToday: {today_date}")
print(f"Type: {type(today_date)}")

# More specific still - day, month, year
# Note that these are properties, not methods
print(f"\nToday: {today_date.day}")
print(f"Month: {today_date.month}")
print(f"Year: {today_date.year}")

# Performing operations with dates
# We can assign a date to a variable
christmas = date(2021, 12, 25)
# christmas is now a date object
print(f"\nChristmas: {christmas}")
print(f"Type: {type(christmas)}")
# Now, we can calculate how many days are between now and Christmas
if christmas != today_date:
    print(f"Only {(christmas - today_date).days} days until Christmas!")
else:
    print("🔔 It's Christmas! 🎄")

days_until_xmas = (christmas - today_date)
print(days_until_xmas)
print(type(days_until_xmas.days))
