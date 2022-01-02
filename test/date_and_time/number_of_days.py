import calendar


def number_of_days(day, month, year):
    days = 0
    weeks = calendar.monthcalendar(year, month)
    for week in weeks:
        if week[day] != 0:
            days += 1
    return days


while True:
    for i, day_name in enumerate(calendar.day_name):
        print(f'{i}: {day_name}')
    try:
        day = int(input("Which day of the week do you want to count?: "))
        if day < 0 or day > 6:
            raise Exception("days not in range")
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
    except Exception as e:
        print("not valid input", e)
        continue

    num = number_of_days(day, month, year)
    print(f'There are {num} of those days in the month and year specified')