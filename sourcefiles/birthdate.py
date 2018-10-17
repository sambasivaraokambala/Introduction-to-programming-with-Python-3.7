#################################################
# Taking birth date as input
# Shiva K
#################################################


birthDay = input("What is your birthdate?(dd/mm/YYYY")

birthDate = datetime.datetime.strptime(birthDay,"%a/%b/%Y").date()

print("Your birth month is " + strftime.birthDate("%B"))
