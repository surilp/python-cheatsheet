from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print(f'todays date is {today}')

print(today.day)
print(today.month)
print(today.year)

print(today.weekday())

today = datetime.now()
print(f'todays datetime is {today}')

today_time = datetime.time(datetime.now())
print(today_time)

# format time
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y"))
print(now.strftime("%B"))
print(now.strftime("%b"))
print(now.strftime("%a"))
print(now.strftime("%A"))
print(now.strftime("%d"))

'''
%y/%Y = Year
%a/%A - weekday
%b/%B - month
%d - day
%c - locale date adn time
%x - locale's date
%X - locale's time

%I - 15 hour
%H - 24 Hour
%M - minute
%S - second
%p - locale's AM/PM
'''

# timedelta

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

timedelta(days=365, hours=5, minutes=1)
datetime.now() + timedelta(days=365)

# replace year
afd = date(today.year, 4, 1)
afd = afd.replace(year=today.year + 1)

# calendars
import calendar

c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)
print(str)

# loop over days of a month

for i in c.itermonthdays(2022, 1):
    print(i)

for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

# first friday every month

for m in range(1,13):
    cal = calendar.monthcalendar(2022, m)
    for week in cal:
        if week[calendar.FRIDAY] != 0:
            print(calendar.month_name[m], week[calendar.FRIDAY])
            break
