#Ask the user to input a complete statement.
#Prints out the word count from the completed statement.

complete_statement = input("Please enter a complete statement: ")
word_counter = len(complete_statement.split()) #Using len to count the numbers and split() to split the statement into words.
print("The counted word from your statement is: ", word_counter) 