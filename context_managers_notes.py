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


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManageFile('notes.txt') as file:
    print('doing some stuff..')
    file.write('this is from my code 😊')