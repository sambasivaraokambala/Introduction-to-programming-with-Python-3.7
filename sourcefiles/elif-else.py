###############################################
# elif-else statements
# Shiva K
###############################################

country = input("What is country of residence?")

# Converting the user input to upper case
country = country.upper()

if country == "CANADA":
    print("Hello")
elif country == "GERMANY":
    print("Guten tag")
elif country == "FRANCE":
    print("Bonjour")
else:
    print("Aloha/Ciao/G'day")
