import calendar

year=int(input("Enter the Year to veiw the calendar:"))
month=int(input("Enter the Month:"))

#to print the entire month of the year
mycalendar=calendar.month(year,month)
print(mycalendar)

#to print the entire year
myyear=calendar.TextCalendar()
print(myyear.formatyear(year))
