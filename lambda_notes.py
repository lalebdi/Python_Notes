# a lambda function is a small one line annonmous that is defined without a name. it has the lambda keyword and arguments and a colon and expression.
# lambda arguments : expression 

add10 = lambda x: x+10

print(add10(5))

#  its the same as a regular function

def add10_func(x):
    return x + 10

# lambda can have multiple args
multi = lambda x,y: x*y

print(multi(4,5))

# they are typically used when you need a smilpe function to be used once or to be used in high order methods

coordinates = [(1,2), (12,7), (5,-1), (10,4)]

points_sorted = sorted(coordinates)
print(coordinates)
print(points_sorted)
#  sorting by the y value below
points_sorted2 = sorted(coordinates, key= lambda x: x[1])
print(points_sorted2)
# sorting by the sum
points_sorted3 = sorted(coordinates, key= lambda x: x[0] + x[1])
print(points_sorted3)

# map function: transforms each element with the a function. has a function as an arg and a sequence. map(func, seq)

a= [1, 2, 3, 4, 5, 6]
# multiplying each element by 2
b = map(lambda x: x*2, a)
print(b)
print(list(b))
# same thing can be achieved with list comprehension
c = [x*2 for x in a]
print(c)

# filter function: gets a sunction and  a sequence. retuns true or false.

d = filter(lambda x: x%2 == 0, a) #getting even numbers
print(d)
print(list(d))
# same thing can be achieved with list comprehension
e = [x for x in a if x%2 == 0]
print(e)

# the reduce function: takes a function and a sequence. it repeatatly applies the function and retuns a single vlaue. Needs to be imported

from functools import reduce

#  getting the product of all the elements
f = reduce(lambda x,y: x*y, a) # the reduce lambd always has 2 args
print(f)

