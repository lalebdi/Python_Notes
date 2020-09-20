from multiprocessing import Pool


# Process Pool: can be used to manage multiple processes. So, a process pool object controls a pool of work processes to which jobs can be submitted and it can manage processes and split data into smaller chuncks that be be managed in parallel by different processes
# most common methods are the map, apply, join and close

def cube(number):
    return number * number * number


if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    result = pool.map(cube, numbers) # this will automatically allocate the max number of processes for you and create different processes. So, this will create a s many processes occur in the machine and then it will split the iterable (numbers) into equal sized chucks and submit this function (cube) which is executed in parallel by different processes. 
#  to have one function executed by the pool use "pool.apply(cube,nubers[0])"

    pool.close() # close should be called before the join
    # below we want to wait for the pool to prcoess all the calsulation and return the results
    pool.join()
    print(result)


#     # with a share value:
#     from multiprocessing import Process, Value, Array, Lock
# import time
# import os

# # to share data between processes. Since they don't share a memory space, the dont have access to the same data. they need spcial memory share object to share data. there are 2 memory share objects that we can use:
# # 1- Value
# # 2- Array

# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1
# # or
#         # lock.acquire()
#         # number.value += 1
#         # lock.release()

# if __name__ == "__main__":

#     lock = Lock()
#     shared_number = Value('i', 0) # takes 2 arguments. 1- is the data type as a string (here its an integer as a string). 2- a starting value.
#     print("Number at beginning is", shared_number.value)

#     # now creating 2 processes that should modify the shared number
#     p1 = Process(target= add_100, args = (shared_number,lock))
#     p2 = Process(target= add_100, args = (shared_number, lock))

# # we start the processes
#     p1.start()
#     p2.start()

#     # wait for them to complete
#     p1.join()
#     p2.join()


    # print('number at the end is ', shared_number.value) # you will get a different number everytime you runs this because the race condition happenened. to prevent it use a lock

# # to share data between processes. Since they don't share a memory space, the dont have access to the same data. they need spcial memory share object to share data. there are 2 memory share objects that we can use:
# # 1- Value
# # 2- Array

# # a Queue can be used for safe data exchanges

# def add_100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         # running a number for loop will give you the same array because you are creating a local variable
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i]+= 1



# if __name__ == "__main__":

#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0, 200.0]) # takes 2 arguments. 1- is the data type as a string (here its a double as a string). 2- a starting list.
#     print("Array at beginning is", shared_array[:])

#     # now creating 2 processes that should modify the shared number
#     p1 = Process(target= add_100, args = (shared_array,lock))
#     p2 = Process(target= add_100, args = (shared_array, lock))

# # we start the processes
#     p1.start()
#     p2.start()

#     # wait for them to complete
#     p1.join()
#     p2.join()

#     print("Array at beginning is", shared_array[:]) # you will get a different number everytime you runs this because the race condition happenened. to prevent it use a lock

# # Queue:
# from multiprocessing import Queue # <-- a Queue follow a linear dat principle that processes first come first served 
# import time
# import os


# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)


# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1 * i)


# if __name__ == "__main__":

#     numbers = range(1, 6)
#     q = Queue()

#     p1 = Process(target= square, args = (numbers, q))
#     p2 = Process(target= make_negative, args = (numbers, q))

# # starting here
#     p1.start()
#     p2.start()
# # joining --> see the comments below for the explanation

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())