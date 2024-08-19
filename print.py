# print("The perimeter of a square with side length 5 is: ", 4 * 5)

# print("The area of a square with a side length of 8 is: ", 8 * 8)

# print("The area of a circle with radius 5 is: ", 3.14 * 5 * 5)

# print("The volume of a sphere with radius 5 is: ", 4/3 * 3.14 * 5 * 5 * 5)


print("Hello!")
print("Hello World")
print("Hello, World", end="!")
print("Hello, World", end="")


print("Hello", "World!")
print("Hello", "World!", sep="&")
print("Hello", "World", "and", "everyone", "who", "lives", "there", sep=" ")

# Does not work as expected with string concatenation
# print("Hello" + "World", sep="&")



first_name = "Branden"
middle_name = "Michael"
last_name = "Bent"

full_name = first_name + " " + middle_name + " " + last_name

print("FULL:", full_name)
print(full_name[7])

# Print just the first name using string slicing
print(full_name[:7])

# Print just the middle name using string slicing ### Notice that the slicing operator will return the characters up to, but NOT including the ending index
print(full_name[8:15])

# Print just the last name using string slicing
print(full_name[16:20])

print(len(full_name))

print()

print(full_name[0:7])


# shortcut to print the first name
print(full_name[0:7]) 
print(full_name[0:len(first_name)])
print(full_name[:len(first_name)])

fn = full_name[:7]
ln = full_name[16:]
print(fn)
print(ln)


print(full_name[:7] + " " + full_name[16:])
print(full_name[:7], full_name[16:], sep=" ", end="!\n")

name = "Branden"
job = "Engineer"

print(name + " is an " + job + ".")
print(name, "is an", job, sep=" ", end=".\n")

# "formatted strings" or "f-strings" allow us to insert variables into strings using curly braces and the "f" prefix
print(f"{name} is an {job}.")


user_input = input("Enter your name: ")
print(f"Hello, {user_input}!")
