#####################################
# Input numbers
# Shiva K
#####################################

# Ask user to enter his salary

salary = input("Enter your salary:")
# Ask user to enter his bonus amount
bonus = input("Enter your bonus amount:")

payCheck = float(salary) + float(bonus)

# print the check
print("your Salary is {0:.3f}".format(payCheck))
