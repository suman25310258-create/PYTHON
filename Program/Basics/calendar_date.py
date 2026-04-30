import calendar

year=int(input("Enter the Year : "))
month=int(input("Enter the Month : "))

#calendar.setfirstweekday(calendar.SUNDAY) #If we want SUNDAY is the 1st day.
cal=calendar.month(year,month)

#cal=calendar.calendar(year) # For all Months

print(cal)