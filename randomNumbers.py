import random

# first will generate pseudo random numbers
# they are re-reproducable

a = random.random()
print(a)

# to have a specific range
b = random.uniform(3,9)
print(b)

# to produce intergers we can use 
c = random.randint(2,8)
print(c)

# to produce integers that will be the same as above but non inclusive
d = random.randrange(2,9)
print(d)

# here will produce statstical random number with a mean of 0 and standard deviation of 1
e = random.normalvariate(0,1)
print(e)

# picking choices
letters = list("ABCDEFG")
f = random.choice(letters)
print(a)

# to pick more than one random unique elememt
g = random.sample(letters, 3)
print(g)

# to pick more than one random non-unique element
h = random.choices(letters, k=3)
print(h)

# shuffle
random.shuffle(letters)
print(letters)

# can use seed to any of the above method to recreate the generated result. pass a number in the seed argument as a key

# # secrets
import secrets

# for passwords, tokens, and auth

# the number in the argument is not included
i = secrets.randbelow(10)
print(i)

# this will retun an integer with k rand bits
j = secrets.randbits(4)
print(j)

# the below choice is non reproduceable
mylist = list("ABDCGHI")
k = secrets.choice(mylist)
print(k)

# # numpy

import numpy as np 
# after you pip install numpy if you still having problems importing numpy consider chnaging the environment

# array with random floats
l = np.random.rand(3) #this will produce a 1d array with 3 elemets
print(l)

#  3 dimention
m = np.random.rand(3, 3) 
print(m)

# random integers in a range

n = np.random.randint(0 ,10, 3) #start, end and size
print(n)

# to get an array with higher dimention use a tuple

o = np.random.randint(0 ,10, (3, 4)) #start, end and size
print(o)

# shuffle
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)

np.random.shuffle(arr)
print(arr)

