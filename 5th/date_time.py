import datetime

print(datetime.date.today())

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.strftime("%d %b %Y"))
print(today.strftime("%A %B %y"))

print(today.strftime("Please attend out event %A, %B %d in the year %Y"))

userInput = input("Please enter your birthday (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)

days = birthday - today
print(days.days)
