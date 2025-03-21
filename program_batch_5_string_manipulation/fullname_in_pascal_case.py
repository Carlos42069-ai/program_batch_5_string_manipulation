#Ask the user for a name.
#Prints out in pascal casing. 

asking_name = input("Please enter your name in incorrect casing: ")
pascal_casing = asking_name.title().replace(" ", "")
print("The fullname inpute in improper casing is now: ", pascal_casing)