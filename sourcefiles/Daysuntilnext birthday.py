#################################################
# Days until next birthday
# Shiva K
#################################################

# import datetime module
import datetime


# Ask the user to give his next birthday date in the specified format
nextbirthDay_Date = input("What is your next birthdate?(dd/mm/YYYY)")

# Convert the user given string date to date datatype using strptime function
nextbirthDay_Date = datetime.datetime.strptime(nextbirthDay_Date,"%d/%m/%Y").date()

# Assigning today's date to currentDate variable
currentDate = datetime.date.today()

# Calculate the difference between the two days(Your next birthdate and today's date)
difference = nextbirthDay_Date-currentDate

# print the result
print("You next birthday is in " + str(difference))
