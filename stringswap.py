man = "Branden"
woman = "Seonhye"
man_woman = man + " " + woman
man_woman_question = man + "?" + woman
# swapped = man_woman[5] + man_woman[1:5] + man_woman[0] + man_woman[6:]
# print("SWAPPED:", swapped)

# the split() method will split the string into a list of words, and the first word can be accessed by using the index operator. Since we did not specify a delimiter, the split method will use a space as the default delimiter
first_word = man_woman.split()[0]
print("First word:", first_word)

first_word_question = man_woman_question.split("?")[0]
print("First word with ?:", first_word_question)

########## Challenge ##########
# Swap the first letter of both names, for the given variables the result should be "Sranden Beonhye". Use the "combined" string man_woman for this challenge

# this gives us the first letter of each name
# swapped_names = man_woman.split()[0][0] + man_woman.split()[1][0] 

# this gives us the first letter of each name, and the rest of the names
# swapped_names = man_woman.split()[0][0] + man_woman.split()[1][1:] + " " + man_woman.split()[1][0] + man_woman.split()[0][1:]

# isntead of an empty string, we can use the join method to join the two strings together. The join method will use the string we call it on as the delimiter, but it will not add the empty string we've specified to strings being concatenated. This seems like a downside, but it actually lets us combine concatonation and listing them without ending up with something weird like "S randen B eonhye"
swapped_names = " ".join([man_woman.split()[0][0] + man_woman.split()[1][1:], man_woman.split()[1][0] + man_woman.split()[0][1:]])

print("SWAPPED NAMES: ", swapped_names)
