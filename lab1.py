# Ask the user for input
single_character = input("Please enter a single character: ")

# Validate input and provide ASCII value
if len(single_character) == 1:
    ascii_value = ord(single_character)
    print(f"The ASCII value of '{single_character}' is {ascii_value}.")
else:
    print("Error: Please enter exactly one character.")

# Extend the program for a string of characters
string_of_characters = input("Now enter a string of characters: ")

print("ASCII values for each character in the string:")
#TODO: Use a loop to print each character and its ASCII value
    ascii_value = ord(char)
    print(f"'{char}': {ascii_value}")
