# a tuple is a collection of a data type that is ordered, immutable and alows duplicate elements. It is similar to a list but it is "read only"
# to access elemets use the index just like a list.
# You cant change the elements in a tuple

my_tuple = ("Max", 28, "Boston") # evedently the parenthesis are optional!!!
print(my_tuple)
print(type(my_tuple))

single_tuple = ("Leah",) # for a single item to be a tuple add a comma at the end. Otherwise, it will be considered a string.
print(type(single_tuple))

# iterable tuple
it_tuple = tuple(["Bella", 9, "New York"])
print(it_tuple)

# iterate in a tuple
for i in my_tuple:
    print(i)

# to check if an element is in the tuple, use an if else statement

if "Max" in my_tuple:
    print("Yaaassss")
else:
    print("No")


# new tuple below
letters = ("a", "p", "p", "l", "e")

# to get the length (number of elements) of a tuple use the len method
print(len(letters))

# to count an element in a tuple (seee how many) use the count method
print(letters.count("p"))

# to find the first index of an elemet use the index method
print(letters.index("p"))

# to convert a tuple to a list or the othe way around use the list or tuple methods
letters_list = list(letters)
print(letters_list)

letters_tuple = tuple(letters_list)
print(letters_tuple)

# slicing in tuples to access parts
a = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 )

b = a[ 2 : 5 ] # if the start is not specified it will start in the beginning and if the end is not specified it will go all the way to the end.
print(b)

c = a[::2] #this will go from the beginnning to the end with a step of 2 ( every second element) you can use a negative step -> will reverse the tuple.
print(c)


# unpacking a tuple
dog = "Snowball", 7, "New York"

name, age, city = dog # the number of elements on the left must match the number of elements in the tuple. Otherwise, it wont unpack.

print(name)
print(age)
print(city)

# we can unpack multiple elemenst with a * -> assign multiple elements to a list.

multi_unpack = (0, 1, 2, 3, 4)

i1, *i2, i3 = multi_unpack

print(i1)
print(i3)
print(i2)

# to compare a tuple to a list. Since a tuple is immutable python is optimized when working with a tuple becuse a tuple is smaller in size than a list.

import sys

a_list = [0, 1, 2, "Boom", True]
a_tuple = (0, 1, 2, "Boom", True)

print(sys.getsizeof(a_list), "bytes")
print(sys.getsizeof(a_tuple), "bytes")

# or

import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1_000_000)) # the _ is like a comma for easy number readablitiy
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1_000_000))
