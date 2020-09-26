# are a great tool for resource management. it allows you to allocate and release resources when you want to. e.g. with-open statment.
with open('notes2.txt', 'w') as file2:
    file2.write('this is from my code 😊😁')


file2 = open('notes2.txt', 'w')
try:
    file2.write('this is from my code 😊')
finally:
    file2.close()

# the code above can be used on databases e.g.:
from threading import Lock
lock = Lock()

lock.acquire()
# do stuff here....
lock.release()

# a simpler way of doing the above is ->
# with lock: # uncomment this
    # do stuff here

# Implementing context managers for our own classes:

# use the enter-exit method
class ManageFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
    def __enter__(self): #this will be executed as soon as we enter the with statment
        print('enter')
        self.file = open(self.filename, 'w') #creating a file here
        return self.file


    def __exit__(self, exc_type, exc_value, exc_traceback): # we see here, the type, vlaue and traceback in the exit method. so you can handle exceptions here and if anything happends that is not true it will be raised  by the "with" statment
        if self.file:
            self.file.close()
        if exc_type is not None: # this is to handle exceptions ourselves. Don't forget the return statment
            print("Exception has been handled")
        print('exc', exc_type, exc_value)
        print('exit')
        return True

with ManageFile('notes.txt') as file:
    print('doing some stuff..')
    file.write('this is from my code 😊')
    file.nonexistmethod() #this is a non existing method here to raise an exception. uncommit to see it in action -> you will see in the exit method it still closed the file.  The "with" statment did not print the continuing. 
print('continuing')


# the above can be implemented as a function 
from contextlib import contextmanager
# we have to use this as a decorator

# the below is a generator function
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w') #this will make sure to allocate the resource
    try: #this is what was in the enter function
        yield f # this will stop whats going on to take it to the "with" statement below. once its done it will comeback to the finally to close and free up the file. Exceptions can be handled here. 
    finally: #here is what was in the exit function
        f.close()


with open_managed_file('notes3.txt') as f:
    f.write('something I did..')
