##########################################
# Multiple or's in a single if statements
# Shiva K
##########################################
import datetime

# Ask the user to enter any date
userDate = input("Enter the date(mm/dd/YYYY)")

#Converting the userDate(string type) to date type
userDate = datetime.datetime.strptime(userDate,"%m/%d/%Y").date()


if userDate.strftime("%B") == "April" or userDate.strftime("%b") == "June" \
or userDate.strftime("%B") == "September" or userDate.strftime("%B") == "November":
    print(userDate.strftime("%B") + " month has 31 days" )
    
