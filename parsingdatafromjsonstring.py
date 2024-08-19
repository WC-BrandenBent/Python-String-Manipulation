########## NOTICE ##########
# THE PURPOSE OF THIS EXERCISE IS TO PRACTICE PARSING DATA FROM A STRING. IMPORTING REQUESTS, MAKING AN API REQUEST, AND WORKING WITH ACTUAL JSON DATA IS A SEPARATE EXERCISE. ANYTHING IN THIS FILE RELATED TO APIs OR JSON DATA IS JUST HERE TO SHOW HOW WE CAN GET DATA IN THE FUTURE. TO GET DIFFERENT DATA SIMPLY CHANGE THE url VARIABLE TO A DIFFERENT API ENDPOINT. DON'T WORRY ABOUT API STUFF OR DOING REQUESTS WITH PYTHON, THAT WILL BE COVERED AT A LATER DATE
########## NOTICE ##########


import requests

# Specify the URL of the API
url = "https://jsonplaceholder.typicode.com/users/1"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
	# Print the response content
	##### FOR FUTURE REFERENCE, this response will actually be of type "list". For practice I am converting it to a string, lists are a big subject and will be revisited another day #####
	# print(type(str(response.json())))
	json_string = str(response.json())

else:
	# Print an error message
	print("Error: Failed to retrieve data from the API")


# The output is a JSON object containing the data multiple users. Each user has and id, username, email and address.
# The address field is a nested object containing the street, suite, city, zipcode and geo fields
# The geo field is a nested object containing the lat and lng fields: below is an example of a single user
# data = 	{
#     "id": 1,
#     "name": "Leanne Graham",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#       "street": "Kulas Light",
#       "suite": "Apt. 556",
#       "city": "Gwenborough",
#       "zipcode": "92998-3874",
#       "geo": {
#         "lat": "-37.3159",
#         "lng": "81.1496"
#       }}}

# print(json_string)

# Split the string into individual user entries
# user_blocks = json_string.split("}, {")
# print (user_blocks)


# From a single user response (after being converted into a string), extract the name of the user and their email address, and print out a string in the following format: "The user <name> can be contacted at <email>"

# first lets remove the curly braces and any whitespace
cleaned_string = json_string.strip("{} ")
# print(cleaned_string)

# Below we're searching for the index of the string "'name': " and adding the length of the string to the index to get the starting index of the name. The len("'name': ") will always be 9, but using the len() function makes it more clear to a reader what we are doing, and lets us change the string without having to change the index down the road
name_starting_index = cleaned_string.find("'name': '") + len("'name': '")

# print(name_starting_index) # 18
# print(cleaned_string.find("'name': ")) # 9
# print(len("'name': '")) # 9

# Now we need to find the ending index of the name. We can do this by finding the index of the next single quote after the starting index
name_ending_index = cleaned_string.find("'", name_starting_index)
# print(name_ending_index) # 31

# Now we know where the name starts ([18])and ends ([31]), so we can extract it from the large string
name = cleaned_string[name_starting_index:name_ending_index]
# print(name) # Leanne Graham

# Halfway done, here is the current output string using the string literal using the f-string method. Using this method will make it easier to expand our code should we decide to parse through multiple users
# print(f"The user {name} can be contacted at ")


# Extracting the email will be very similar to extracting the name, but we will need to find the index of the email field instead of the name field
email_starting_index = cleaned_string.find("'email': '") + len("'email': '")
email_end_index = cleaned_string.find("'", email_starting_index)

email = cleaned_string[email_starting_index:email_end_index]

print(f"The user {name} can be contacted at {email}")

