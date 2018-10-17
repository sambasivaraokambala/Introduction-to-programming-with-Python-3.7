#################################################
# And and Or in a single if statement
# Shiva K
#################################################

country = input("Enter your country:")
pet = input("Enter your pet:")

country = country.upper()
pet = pet.upper()

if country == "CANADA" and \
   pet == "MOOSE" or \
   pet == "BEAVER":
    print("Would you like Hockey as well?")
