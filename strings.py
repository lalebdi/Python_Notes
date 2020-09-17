# a string is a ordered, immutable data type that is used for text representation. 

# triple quotes are use for multi line string. 

# to access characters or substring. its the same as list. use []

string1 = "I love brisket" # you can't change a character because strings are immutable
char = string1[0] # a negative index can be used to start from the end
print(char)

# you can access a sub string by slicing

substring1 = string1[2:6] # the 6 is excluded
substring2 = string1[7:] # can use a step here, e.g. 2 for every other character. a negative step will reverse a string
print(substring1)
print(substring2)

#  to concatinatestring use +
string2 = "and bacon"

my_loves = string1 + " " + string2

print(my_loves)

# to iterate over a string with a for in loop:

for i in my_loves:
    print(i)

# to check if a character is in a string use if statement:
if "e" in my_loves: # YOU CAN CHECK FOR SUBSTRINGS
    print("yup")
else:
    print("Nope")

# to trim white space
string3 = "         Boom Roasted             "
stripped_string = string3.strip() # it doesn't change the string because they are immutable
print(stripped_string)

# to convert to uppercase
upper = string1.upper()
print(upper)

#  to convert to lower case
lower = string2.lower()
print(lower)

# to check if the string starts with a character or a substring (case sensitive)
print(string1.startswith("I"))

# to check if the string ends with a character or a substring (case sensitive)
print(string1.endswith("bacon"))

# to find the index of a character or a substring (case sensitive)
print(string1.find("r"))

# to count the number of characters or substring (case sensitive)
print(string1.count("i"))
print(string1.count("e"))

# to replace characters or substrings
replaced_char = string1.replace("brisket", "bacon")
print(replaced_char)

# lists and strings

string4 = "I love pasta"
string5 = "She,loves,wine"

# to convert a string into a list with each word as an element in a list

string_to_list = string4.split() # by default it will use the space as a splitting site. if commas are there it will put them in a single list. 
print(string_to_list)

string_to_list2 = string5.split()
string_to_list3 = string5.split(",")
print(string_to_list2)
print(string_to_list3)


# to convert a list to a string
list_to_string = " ".join(string_to_list) # putting a spcae between the " " will create a space between the elements
print(list_to_string)

#  the join method is better than using a for in loop -> faster

# formatting strings:

# old method using %
name = "Bella"
my_dog = "a dog named %s" % name # the % tells the interpeter that it is a place holder with a string (s) and the place holder is filled with the variable name. if the vaiable name is a number, instead of a string, then use "d" instead of "s". Use "f" if the variable is a float (to limit the decimals, addthe number of decimals you want between the % and the f. e.g. %2f).
print(my_dog)

# other method is .format()

name2 = "Snowball"
famous_for= "barking none stop"
my_dog2 = "my other dog is {} . {}".format(name2, famous_for) # to specify the decimals use {:2f}
print(my_dog2)

# new method using f-Strings (its like template literals in JS!!)

name3 = "Maruysa"
hates = "fish"
my_dog3 = f"{name3} doesn't like {hates}"
print(my_dog3)