# arguments vs. parameter:
# parameters are the varibales that are defined or used inside parenthesis that are defining the functions.
# arguments are the values passed for these parameters when calling a function.

def print_name(name):
    print(name)

print_name("Leah")

# positional and keyword arguments:

def whatever(a, b, c):
    print(a, b, c)

# calling the function with a posisional argument
whatever(c= 3,b= 2,a= 1) # since the arguments are positional the order doesn't matter 
#  above the keywords matter not the position
#  you can mix them up if you want but you cannot use another positional argument after a keyword argument.

# you can add default argument: they must be at the end 
def whatever2(a, b, c, d= 4):
    print(a, b, c, d)

whatever2( 4, 5, 6)
whatever2( 4, 5, 6, 7)

# variable length argument: 
def whatever3(a, b, *args, **kwargs): # if you mark a param with one * then you can pass any number of posisitonal arguemnts in that function. if ** then you can pass any number of key word arguments in this function.
    print(a,b)
    for arg in args: #its a tuple
        print(arg)
    for key in kwargs: # its a dictionary
        print(key, kwargs[key])


whatever3(1, 2, 3, 4, 5, six = 6, seven = 7)

# forced keyword argument: for keyword only argument. 

def whatever4(a, b, *, c, d): #any param after the star must be a keyword argument
    print(a, b, c, d)

whatever4(9,8, c= 7, d= 4)

def whatever5 (*args, last):
    for arg in args:
        print(arg)
    print(last)

whatever5(7, 5, 3, last = 100)

# unpacking arguments: 
def whatever6(a, b, c):
    print(a, b , c)

my_list = [0, 1, 2] # the length of the container must match the number of paramters
whatever6(*my_list) # also works in tuples the same way
my_dict = { "a" : 6, "b" : 5, "c" : 4} # the keys names must match the paramters in the function
whatever6(**my_dict) # use 2 stars for a dict

# local vs. global variables:

def whatever7():
    x = num
    print('the number inside is ', x)


num = 0
whatever7()

#  to modify the global number:

def whatever8():
    global num
    x = num
    num = 3
    print('the number inside is ', x)


num = 0
whatever8()
print(num)

# passing paramters:
# 2 rules: the params parsed in are a refernce to an object but the refernce is passed by a value. mutable objects (like lists and dictionaries) can be changed in a method but if you rebind the refernce in the method then outer refernce will still point to the oirignal object. Immutable objects (like string and integers) cannot be changed with a method but immutable object contained in an immutable object can be reassigned within a method

def whatever10(x):
    x = 5

var = 15
whatever10(var)
print(var) # did not change

def whatever11(a_list):
    a_list.append(444)

the_list = [333, 222, 1111]
whatever11(the_list)
print(the_list) #changed here

