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

# pop mehtod can be used to retun an arbit. element and removes it
print(my_set4.pop()) 

#  the clear method will clear the set

# to iterate in a set use a for in loop:
for i in my_set:
    print(i)

# to check if an element is present in the set use an if in statement
if 1 in my_set:
    print("yass")

# Union and intersections:
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = { 2, 3, 5, 7}

# to calculate a union:
# a union combines elemets from 2 sets without duplication

u = odds.union(primes)
print(u)

# to calculate the intersection of 2 sets:
#  an intersection will only take elemenst that are found in 2 sets. will use only the elemets found in both sets.

t = odds.intersection(evens)
print(t)

i = odds.intersection(primes)
print(i)

# to calculate the difference in 2 sets
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}

# the difference will retun a set with elements from the first that are not in the second

diff = set_a.difference(set_b)
print(diff)

diff2 = set_b.difference(set_a)
print(diff2)

# the symmetric difference method will retun all the elements  from set a and set b  but not the elements in both sets.

sym = set_a.symmetric_difference(set_b)
print(sym)

#  all of the above mehtods will not modify the sets. 
# to modify the sets in place:

set_a.update(set_b) #merged the 2 sets without duplication
print(set_a)

# the intersection update method will update the set by keeping only the elemets found in both sets.

set_a.intersection_update(set_b)
print(set_a)

# the difference update method will update the set by removing the elements found in another set. So, will grab the non duplicates.
set_a.difference_update(set_b)
print(set_a)

# the symmetric difference update will update the set by only keeping the elements found in set a and set b BUT not the elements found in both

set_b.symmetric_difference_update(set_a)
print(set_b)

# subsets and disjoined
set1 = {1, 2, 3, 4, 5, 6}
set2 = { 1, 2, 3}
set3 = {7, 8}

# subset means all the elements in the first set are found in the second set
print(set1.issubset(set2))
print(set2.issubset(set1)) # true because all the elements in set 2 are in set 1

# super set will return true if all the first set contains all the elements in the second set
print(set1.issuperset(set2))

# isdisjoinet retuns true if both sets are null intersection

print(set1.isdisjoint(set2)) # false because they have the same elements
print(set1.isdisjoint(set3)) # true because they dont have the same elements

# copying

set2 = set1 # if you modify any one of these sets the other will be modified as well
print(set2)
set2.add(7)
print(set2)
print(set1)

# to make an actual copy use the copy method

set3 = set2.copy()
print(set3)

# or use the set method and use the original set (the one you want to copy) as an argument.

set4 = set(set3)
print(set4)

# the frozen set -> a collection data type BUT it is immutable
freeze = frozenset([1, 2, 3, 4, 5, 6,])

print(freeze)

# note that you cannot change the set in frozenset. its like a read only set. Union, difference and intersection method will work. 