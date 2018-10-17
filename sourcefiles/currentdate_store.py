#################################################
# A program to store a today's date in a variable
# Shiva K
#################################################


#importing datetime class
import datetime
 
# Stores today’s date in a variable
currentDate = datetime.date.today()

# prints currentDate
print("Today's date : " + str(currentDate))


# prints current day
print("Today's date is :" + str(currentDate.day))

# prints the year
print("This year is :" + str(currentDate.year))

#prints current month
print("This month is:" + str(currentDate.month))
