#################################################
# Taking birth date as input
# Shiva K
#################################################
import datetime

birthDay = input("What is your birthdate?(dd/mm/YYYY)")

birthDate = datetime.datetime.strptime(birthDay,"%d/%m/%Y").date()

print("Your birth month is " + birthDate.strftime("%B"))
