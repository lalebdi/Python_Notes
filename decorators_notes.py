# Decorators: its a function that takes another function as an argument and extends the behavoir without modifying it. i.e it allows you to add a new functionality to an already existing function.
# function and class 
# function decorators are more common. example:

# note that functions in python are first class objects. i.e like any other object they can be defined inside another function, pass into another function or returned in another function

def start_end_decorator(func): #this is the decorator

    def wrapper():
        print("Start")
        func()
        print('End')
    return wrapper


def print_name():
    print('Angel')

print_name = start_end_decorator(print_name)
print_name()

# or can be done this way:
import functools

def start_end_decorator2(func): #this is the decorator

    @functools.wraps(func) #this will preserve the info of the used function
    def wrapper(*args, **kwargs): #you need the same arguement here or you will get a type error. args and kwargs allows you to use as many arguments as you want
        print("Start")
        result = func(*args, **kwargs) #you need the same arguement here or you will get a type error. args and kwargs allows you to use as many arguments as you want. if the return is not saved in a varibale you will get a none in the terminal.
        print('End')
        return result # you have to retun the variable here
    return wrapper

@start_end_decorator2
def add5(x):
    return x + 5


results = add5(1)
print(results)
# print(help(add5))
print(add5.__name__)


# @my_decorator
# def do_something(): #this function is extended with the function above
#     pass

# this is another example

# import the func tools
def repeat(num_times):

    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
    



@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greeting = greet("Natasha")
print(greeting)

# Nested decortators:  

# have to import the func tools
def start_end_decorator3(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start2")
        result = func(*args, **kwargs)
        print("END 2")
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #it extracts the name and prints the args and kwargs info
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}=(v!r)" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator3
def say_hello(name):
    greeting = f"Hello{name}"
    print(greeting)
    return greeting

say_hello("Ron")


# Class decorators:
# do the same as function deco but they are used to maintain and update a state.
# typical use case: to implement timer decorator to calculate the execution time. Use a debug decorator to print out more info about the call function. can use check decorator to check if the arguments fulfill some requirements and the depth of behavior. Register functions like blckins or cashe the return values or add info or update the state. 

class CounterCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    
    def __call__(self, *args, **kwargs): #this is important in class decorators
        # print("Hi there")
        self.num_calls +=1
        print(f"This is executed {self.num_calls} times")

# cc = CounterCalls(None)
# cc()

@CounterCalls
def say_hello2():
    print("Hello")

say_hello2()
say_hello2()