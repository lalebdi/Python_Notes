# Generators are functions that retun an object the we can iterate over. they generate the items inside the object lazyly i.e they generate the items one at a time and only when yu ask for them. So, they are efficient.
#  its like a value but instead of return it ues yield


def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()
print(g)

# for i in g:
#     print(i)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

#  if you run the next(g) again you will get a stop iteration error becuse a generator object will always raise this stop iteration if it does not reach a yield statement

# generators can used as inputs to funcotins that take iterables.

print(sum(g)) # will calculate the unused yields i.e how many times the yields where not called. comment the value varibale and see.

print(sorted(g)) # will retun a new list of all the objects in a sorted order

def count_down(num):
    print("starting")
    while num > 0:
        yield num
        num -=1


cd = count_down(4)
print(next(cd))
print(next(cd))
print(next(cd))


#  the big advantage is that they are memory efficient.

def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(first_n(10))
print(sum(first_n(10)))

# compare the above to the generator below:

def first_n_gene(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(first_n_gene(10))
print(sum(first_n_gene(10)))


# Another example

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ....
    a, b = 0, 1
    while a < limit:
        yield a 
        a, b = b , a + b

fib = fibonacci(30)
for i in fib :
    print(i)

# generator expressions: they are written the same way like list comprehensions but with ( ) instread of []

mygenerator = ( i for i in range(10) if i % 2 == 0) # here i can use an expression with a for in loop
#  the above will put all the even numbers in a generator object

for i in mygenerator:
    print(i)

mylist = [ i for i in range(10) if i % 2 == 0]
print(mylist)


# to convert the generator output into a list
mygenerator2 = ( i for i in range(10) if i % 2 == 0)
convert = list(mygenerator2)
print(convert)