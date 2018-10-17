#################################################
# Alerting a user about expiration of milk using timedelta function
# Shiva K
#################################################

# import datetime module
import datetime


# Assign the today's date to currentDate variable
currentDate = datetime.date.today()

# Add 15 days to the current date 
expire_date = currentDate + datetime.timedelta(days = 15)

# print the result by formatting using strftime function
print("Your expiration date is "  + expire_date.strftime("%d,%B"))
