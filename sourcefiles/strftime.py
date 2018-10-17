#################################################
# Dispalying a wedding invite
# Shiva K
#################################################


#importing datetime class
import datetime
 
# Stores today’s date in a variable
currentDate = datetime.date.today()

# prints the invite
print(currentDate.strftime("please attend our event on %A,%B %d in the year %Y"))


