#Ask the user for an improper name.
#Prints out in snake case.

asking_name = input("Please enter your name in incorrect casing: ")
snake_casing = asking_name.lower().replace(" ", "_")
print("The name that you entered is now in snake case formatting: ", snake_casing)