from gettext import find


string = "computer"


# Strings are a sequence of characters, and with python we can be treated as an array of single characters
print(string[0])

print(string[1])

print(string[2])


# Below are slicing operators that allow us to work with specific parts of a string, notice we can use the colon operator to specify a range of characters from the beginning of the string, or exclude those characters and work with the rest of the string with a trailing colon
print(string[:3])

print(string[3:], "testing")

# We can also use the slicing operator to work with a range of characters in the middle of a string instead
print(string[1:4])

# We can also use the slice function to create a slice object that can be used to slice a string. Printing out "slice(1, 4)" may not work as expected, because this method does not return a function, rather a "slice" object. The proper way to use this is to then pass this object to the string object to slice the string, similar to the previous examples
slice = slice(1, 4)

print(string[slice])


# strip(), lstrip(), and rstrip() are methods that can be used to remove whitespace from the beginning, end, or both ends of a string. This is useful when working with user input, as the user may accidentally add whitespace to the beginning or end of their input
# string() will remove whitespace from the beginning and end of a string if you do not give it any arguments
# lstrip() will remove whitespace from the beginning of a string
# rstrip() will remove whitespace from the end of a string

# string_computer = "   computer   "
# print(string_computer)
# print(string_computer.strip())

# you can pass a string into these methods to remove those characters rather than whitespace
# random_garbage = "!!!???ffddsss,,,,///...!!!!computerfffdddsss,,.,/??!!!"
# print(random_garbage)
# print(random_garbage.strip("!?,./"))
# print(random_garbage.strip("!?,./fds"))

# # if you are removing more than symbols from the string you need to keep in mind what you are looking for. Passing in the characters "c" or "r" will remove those from the word, and since the word is "computer" it won't give us the string we are looking for
# print(random_garbage.strip("!?,./fdscr"))

# # we CAN however pass in any other less inside of the string and it won't touch them, strip() will only remove the characters from the beginning and end of the string
# print(random_garbage.strip("!?,./fds ompute"))

# # since we are not using the default strip() argument and removing just white space, we need to add a whitespace character to the strip() method. All we have to do is add a literal space to the string we are passing in, nothing fancy
# random_garbage_with_whitespace = "  !!!  ???ff  ddsss,,,,///...!!!!computer   fffdddsss,,.,/??  !!!  "
# print(random_garbage_with_whitespace.strip("!?,./fd sompute"))


# we can use the find() method to search for a specific substring within a string. The find() method will return the index of the first occurrence of the substring, or -1 if the substring is not found
find_welcome_string = "Hello, welcome to my world."

temp = find_welcome_string.find("welcome")

print("welcome from find():", temp)

# a trick we can use to find the entire word from the string is to use the length of that word and add it to the index that find() returns, since we'll have the starting index (from the find() method) and the ending index (from the length of the word) we can extract the word from the string

print(find_welcome_string.find("welcome")) # returns 7
print(len("welcome")) # returns 7, so we know that the word welcome starts at index 7 and ends at index 14

print(find_welcome_string[7:14])