# the itertools module is a collection of tools to handle iterators. Iterators are data types that can be used in a for loop. 
# Itertools are: product, permutations, combinations, accumulate, groupby, and infinite iterators.


#  products
# import first:

from itertools import product

a = [1, 2]
b = [3 , 4]

prod = product(a,b) # combines 1 with 3 then 1 with 4 and 2 with 3 then 1 with 4
prod2 = product(a,b, repeat= 2) 
print(prod)
print(list(prod))
print(list(prod2))


# permutations:
# will return all possible orderings of an input
# import it
from itertools import permutations

c = [1, 2, 3]
perm = permutations(c)
perm2 = permutations(c, 2) # to specify the length of the permutation
print(perm)
print(list(perm))
print(list(perm2))

# combinations
# wil make all possibly combinations with a soecified length without reptetitons
# import
from itertools import combinations, combinations_with_replacement

d= [1, 2, 3, 4]
comb = combinations(d, 2) # the second arg is a must
print(list(comb))

comb_wr = combinations_with_replacement(d,2) # this allows repetitions
print(list(comb_wr))


# accumulate
# makes an iterater that retuns accumulated sums
# import

from itertools import accumulate
import operator # to multiply the elements

e = [ 1, 2, 3, 4]
accu = accumulate(e) # output = 1, 1+2, (1+2)+3, ((1+2)+3)+4. by default it will compute the sums
print(list(accu))


accu2 = accumulate(e, func=operator.mul)
print(list(accu2))

e2 = [ 1, 2, 5, 3, 4]

accu3 = accumulate(e2, func=max)
print(list(accu3))


# groupby:
# makes an iterator that returns keys and groups
# import it

from itertools import groupby

def smaller_than_3(x):
    return x< 3

f = [1, 2, 3, 4]
group_obj = groupby(f, key=smaller_than_3)
# print(list(group_obj))

for key, value in group_obj:
    print(key, list(value))

# can use a lambda in the groupby
# a lambda functions are small one line functions that can have an input and an expression and return an output
f2 = [1, 2, 3, 4]
group_obj2 = groupby(f2, key=lambda x: x<3)
for key, value in group_obj2:
    print(key, list(value))

users = [{'name' : 'jessica', 'age': 25}, {'name' : 'Samira', 'age': 25}, {'name' : 'Shani', 'age': 23}, {'name' : 'Stefani', 'age': 21}]

group_users = groupby(users, key=lambda x: x['age'])
for key, value in group_users:
    print(key, list(value))


# infinite iterators
#  count, cycle, repeat
# import

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 20:
        break

h = [1, 2, 3]
for i in cycle(h):
    print(i)
    if i == 3: # it will cycle through the list infinately unless you add a break
        break

for i in repeat(h, 2):
    print(i)

