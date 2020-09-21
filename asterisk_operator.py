# it can be used for :
# multiplication
# creating tuples and lists with repeated elements
# args and kwargs and keyword only parameters
# for unpacking list, tuples and dicts into function arguments
# unpacking containers and merging containers into a list or dict

zeros = [0, 1] * 10
print(zeros)

abz = "AB" * 12
print(abz)

def funcy(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

funcy(44,55, 3, 4, 5, six = 66, seven = 77)

def funky(a, b, *, c):
    print(a, b, c)

funky(1, 2, c = 55)

def funky2(a, b, c):
    print(a, b ,c)

my_list = [00, 11, 22]
funky2(*my_list)

my_dict = {"a": 44, "b":66, "c": 22} # the number of keys must equal the number of params and the keys must match the params
funky2(**my_dict)

numbers = [1, 2, 3, 4, 5, 6] # if it is a tuple it will be unpacked into a list

*begninning, last = numbers
print(begninning)
print(last)

begninning, *last = numbers
print(begninning)
print(last)

begninning, *middle, last = numbers
print(begninning)
print(middle)
print(last)

my_tuple = (44, 55, 66)
listy = [77, 88, 99] # can be used with a set as well

new_list = [*my_tuple, *listy]

print(new_list)

dict_a = {'a': 33, 'b' : 55}
dict_b = {'c' : 22, 'd': 44}
dict_c = {**dict_a, **dict_b}
print(dict_c)


