#################################################
# Accessing time using datetime.datetime.now() function
# Shiva K
#################################################

# import datetime module
import datetime


# Assign the current time to currentTime variable
currentTime = datetime.datetime.now()

#print the result
print(currentTime)

# print the hour part
print(currentTime.hour)


#print the minute part
print(currentTime.minute)

#print the second part
print(currentTime.second)
