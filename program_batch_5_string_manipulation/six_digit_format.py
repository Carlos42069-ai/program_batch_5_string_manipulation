#Ask user for number 1-1000
#Make an if else statement with a condition that inly enters 1-1000
#Print in a 6 digit format

enter_num = int(input("Please enter a number from (0-1000): "))
if 0 <= enter_num <= 1000:
    add_zero = f"{enter_num:06d}"
    print("The number is: ", add_zero)

else:
    print("Please enter a valid input")