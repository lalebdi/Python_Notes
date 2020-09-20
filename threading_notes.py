# threading:
from threading import Thread, Lock, current_thread
import time

#  threads share data since they live in the same memory space. So, instead of the function below we will use a global variable.

database_value = 0 #this will simulate a data base

def increase(lock): # this will modify the golbal variable
    global database_value

    lock.acquire() # you can use the syntax "with lock:" and insert the code underneath to remove the lock release( )
# below will simulate some database access and get the value from the database and have a copy of it
    local_copy = database_value

    # processing 
    local_copy += 1
    time.sleep(0.1)
# below will copy back the data
    database_value = local_copy
    lock.release() # every time you lock acquire you have to release at the end otherwise you will lock your code and will be stuck

    # got start value of 0 and end value of 1 instead of 2 and that is due to a raise condition, which happens when 2 or more threads try to modify a variable at the same time. To prevent this we use the Lock from threading which prevent a thread from accessing the incease() code.

if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target= increase, args= (lock,))
    thread2 = Thread(target= increase, args= (lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')




# # queues are excellent for thread safe and process safe data exchanges and data processing in multi processing and multi threading. You need to import queue
from queue import Queue

# # Queue is a linear data structure that follows the first in first out principle. e.g. its like a real life queue (first come first serverd)

if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get() # this will get and remove the first item
    print(first)

    # in a threading environment whenever you do q.get and process this object you should always call the below method
    q.task_done()
    q.join() # this will block untill all the queues have been processed and it is similar to thread.join() method 
    print(q.empty()) # to check if the queue is empty  --> will retun truw if the queue is empty
    print("End of Queue main")

# a Queue example: (to run the code below comment the above code except the Queue import line 47)

def worker(q, lock):
    while True: #this is an infinate loop that is starting 
        value = q.get() # this will block and wait until the items are avaiable

        # processing:
        with lock:
            print(f"we are in {current_thread().name } got {value}")
            q.task_done()

if __name__ == "__main__":

    q= Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target= worker, args= (q, lock))
        thread.daemon = True # we are using the daemon thread here that will die when the main thread dies since we have an infinate loop above. it is false by default and if left that way yuo will be suck in an infinate loop. 
        thread.start()
    
    # We have to fill our Queues with elements
    for i in range(1, 21):
        q.put(i)

    q.join() #we want to block and wait untill all the items have been processed

    print("End of the Queue example main")











# # starting code below:
# def square_numbers():
#     for i in range(100):
#         i * i 


# if __name__ == "__main__":
#     threads = []
#     num_threads = 10

# # create threads
# for i in range(num_threads):
#     thread = Thread(target= square_numbers)
#     threads.append(thread)


# # start threads
# for thread in threads:
#     thread.start()

# # join threads: wait for them to complete
# for thread in threads:
#     thread.join()

# print("End Main")