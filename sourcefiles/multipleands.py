########################################
# Multiple and conditions
# Shiva K
########################################

favMovie = input("Enter your favourite movie:")
favBook = input("Enter your favourite Book:")
favEvent = input("Enter your favourite Event:")

favMovie = favMovie.lower()
favBook = favBook.lower()
favEvent = favEvent.lower()

if favMovie == "star wars" and \
   favBook  == "lord of the rings" and \
   favEvent == "comicon" :
    print("You and I should hangout") 
