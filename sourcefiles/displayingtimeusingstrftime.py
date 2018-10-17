#################################################
# Display the time using strftime function
# Shiva K
#################################################

# import datetime module
import datetime


# Assign the current time to currentTime variable
currentTime = datetime.datetime.now()

#print the result
print(datetime.datetime.strftime(currentTime,"%H:%m:%S %p"))

