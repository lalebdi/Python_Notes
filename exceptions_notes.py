# The difference between a syntax error and an exception

# syntax error: when the parser detects a syntactically incorrect statement
# like this:
# a = 5, print(a)

# exceptions is when a statment is syntactically correct but might cause an error when executed.
# many types:
# type error: adding a number to string
# a = 5 + "10"

# import error:
# import somemodule that does not exist
# it will raise module not found error.

# name error:
# a = 5
#  b = c 
#  the c is not defined
# it will raise a name error

# file not found error:
# f = open('somefile.txt')
#  will raise a file not found error.

# the value error:
# happens when if the function receives the right type but wrong vlaue
# a = [1, 2, 3]
# a.remove(1) -> this is fine
# a.remove(4) -> will raise a value error

# index error:
# when trying to access an index in a list that is not too large
# a[4] -> will raise an index error

# my_dict = { "name" : "Ron"}
# my_dict["age"] -> will raise a key error


# raising an exception:
# when you want to force an exception to occur when a certain condition is met. can be done using raise keyword.

# x = -5
# if x < 0:
#     raise Exception('x should be positive')

# another way is using the assert statement. will throw an assertion error if the assertion is not true

# x = -3
# assert (x >= 0), 'x is not positive -> will raise an assertion error. add a guiding message after

# to handle exception (catch exceptons with try - except block )

# try:
#     a = 5 /0 # -> raises a zero division error
# except: -> can catch the type of exception by adding "Exception as e" after the except
#     print('an error happened')

# try:
#     a = 4/0
# except Exception as e:
#     print(e)

# it's good practice to pridect the error
# try:
#     a = 4/1
#     b = a + "5"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

# you can have an else clause to continue if nothing is wrong

# try:
#     a = 4/1
#     b = a + 5
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("eveything is fine")

# you can also have a finally clause; runs always no matter if there is an exception or not. used for clean up


# try:
#     a = 4/1
#     b = a + 5
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("eveything is fine")
# finally:
#     print("cleaning up....")

# defining our own exceptions:
# by subclassing from the base exception class

class ValuseTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_vlaue(x):
    if x > 100:
        raise ValuseTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)
try:
    test_vlaue(200)
except ValuseTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)