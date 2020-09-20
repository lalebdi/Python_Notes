from multiprocessing import Process, Value, Array
import time
import os

# to share data between processes. Since they don't share a memory space, the dont have access to the same data. they need spcial memory share object to share data. there are 2 memory share objects that we can use:
# 1- Value
# 2- Array

def add_100(number):
    for i in range(100):
        time.sleep(0.01)
        number.value += 1



if __name__ == "__main__":
    shared_number = Value('i', 0) # takes 2 arguments. 1- is the data type as a string (here its an integer as a string). 2- a starting value.
    print("Number at beginning is", shared_number.value)

    # now creating 2 processes that should modify the shared number
    p1 = Process(target= add_100, args = (shared_number,))
    p2 = Process(target= add_100, args = (shared_number,))

# we start the processes
    p1.start()
    p2.start()

    # wait for them to complete
    p1.join()
    p2.join()

    print('number at the end is ', shared_number.value) # you will get a different number everytime you runs this because the race condition happenened. to prevent it use a lock