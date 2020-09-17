# sets are data collection type that is unordered, mutable and allows duplicates. it is created with { } without keys or values just elements separated by a comma.

my_set = {1, 2, 3, 1, 2}
print(my_set)

# can use the set method as an iterable

my_set2 = set([1, 2, 3])
my_set3 = set("Hello") # it will be unordered and only a single L. can be used to find out how many charaters in a word.
print(my_set2)
print(my_set3)

# to create an empty set

my_set4 = {}
print(type(my_set4)) # it will show it as a dictionary as dictionary is a default in python.
# if you want to force the set type use the set method:
my_set4 = set()
print(type(my_set4))

# it is mutable. So, you can add elements using the add method

my_set4.add(1)
my_set4.add(2)
my_set4.add(3)
print(my_set4)

#  to remove elements use the remove method:
my_set4.remove(3)
print(my_set4)

# the discard method will remove the element. If the elements is not present in the set it will not throw an error
my_set4.discard(4)
print(my_set4)