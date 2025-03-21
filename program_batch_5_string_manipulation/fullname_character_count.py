#Ask the user for a name.
#Print the count of characters inputed by the user.

asking_name = input("Please enter your name: ")
character_counter = len(asking_name) #the len function counts the characters of the inputed name.
print("The total characters that you have input is: ", character_counter)