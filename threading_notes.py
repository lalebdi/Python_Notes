# threading:
from threading import Thread
import time

#  threads share data since they live in the same memory space. So, instead of the function below we will use a global variable.

database_value = 0 #this will simulate a data base

def increase(): # this will modify the golbal variable
    global database_value

# below will simulate some database access and get the value from the database and have a copy of it
    local_copy = database_value

    # processing 
    local_copy += 1
    time.sleep(0.1)
# below will copy back the data
    database_value = local_copy

if __name__ == "__main__":

    print('start value', database_value)

    thread1 = Thread(target= increase)
    thread2 = Thread(target= increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')




















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