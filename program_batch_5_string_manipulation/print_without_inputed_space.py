#Define variable name asking for name with several spaces 
#Make a code that removes the following spaces of the entered name
#Print the inputed name without space

your_name = input("Please enter your name with spaces: ")
remove_space = your_name.strip()
print("This is your name without spaces:", remove_space)