# Write a program to create a new string made of an input string’s first, middle, and last character.
# For example: a string "Computers" will output "Cus"
# For practice use a string with an odd number of characters

# string = "dinosaurs"

# new_string = ""

# # get first character then add it to our new string
# first = string[0]
# new_string += first
# # this is the same as the line above but more concise, we've seen the same += operator in in Javascript
# # new_string = new_string + first

# # get middle character # // is the floor division operator, which will return the integer value of the division, and not the float value
# middle = string[len(string) // 2]
# new_string += middle

# # without the floor division operator you have to cast to an int before passing it to the index operator
# # middle = string[int(len(string) / 2)]

# # an alternative method would be to get the middle INDEX of the string, and then get the character at that index
# # middle_index = len(string) / 2
# # new_string += string[int(middle_index)]


# # get last character. DON'T just count the characters, use the len() function. If you count the characters and the string changes, you will have to change the count, or if you attempt to use this same code with a massive string it will be difficult to count the characters
# last = string[len(string) - 1]
# new_string += last

# print(new_string)



# Perform the same task above, except this time the new string should have three ??? characters between each character
# For example: a string "Computers" will output "C???u???s"
# string = "dinosaurs"

# new_string = ""

# first = string[0]
# middle = string[len(string) // 2]
# last = string[len(string) - 1]

# # This is the obvious way to do it... but what if I gave you a string with 200 characters and asked you to put 400 characters in between each of them instead of "???"...
# # new_string += first + "???" + middle + "???" + last


# # The join operator is much better here and will allow us to do this in one line, and it will be much easier to change in the future if we need to
# new_string = "???".join([first, middle, last])
# print(new_string)


########## Challenge ##########
# Allow the user to input the a string, AND the characters they would like to use to separate the characters in the new string and print the result

print("Enter a string and the characters you would like to use to separate the characters in the new string")
string = input("Enter a string: ")

string = string.strip()

# string = string.strip() would work if we knew the user would only ever enter whitespace before and after our string. To prevent user error we should try and be a little more clever and account for the possibility of needing to remove more than just whitespace
# importing the re module gives us access to regular expressions, which can be used to remove all characters that are not letters from the string. The regex is checking for any character (the ^ symbol is a negation operator) that is not a lowercase -a-z- or uppercase -A-Z- letter. The second argument is an empty string, which will replace any character that matches the regex with an empty string. The third argument is the string we are performing the substitution on
# import re
# string = re.sub(r'[^a-zA-Z]', '', string)

print(string)

first = string[0]
middle = string[len(string) // 2]
last = string[len(string) - 1]

new_string = "???".join([first, middle, last])
print(new_string)