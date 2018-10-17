##################################################
# Boolean variables
# Shiva K
##################################################

deposit = input("Enter deposit amount:")
freeToaster = False
if float(deposit) > 100:
    freeToaster = True

if freeToaster:
    print("Enjoy your free Toaster")
    
