# a process is an instance of a program (e.g. a Python interpreter)
# a thread is an intenty within a process that can be scheduled (AKA "lightwieght process") . So, a process can have multiple threads inside.

# processes take advvantage of multiple CPUs and cores.
#  processes take a separate spcae. So, no memory sharing.
# processes are great for CPU-bound processing. 
# New procwss is started indenpendently from other processes.
# yu can interrupt or kill a process.
# One GIL (Global Interpter lock) for each process. that way it avoids GIL limitation.

# However:
# they are heavy.
# starting a process is slower than starting a thread
# they occupy more memory -> remember the no memory sharing.
# the Inter-Process Communication (IPC) is more complicated.

# Talking about threads:
# All thread can share memory.
# light weight
# starting a thread is faster than starting a process.
# Great for I/O-bound (input-output) tasks.

# However:
# Threading is limited by the GIL: One thread at a time.
# No effect for CPU-bound tasks.
# you can't kill it nor interrupt it. memory leaks
# careful with race conditions (occurs when  2 more try to modify a variable at the same time causing a crash).

# GIL: Global interpreter lock
# A lock that allows only one thread at a time to execute in Python.
# Needed in CPython because memory management is not thread-safe.

# To avoid the GIL:
# Use multi-processing.
# Use a different, free-threaded Python implementation like Jython.
# Use Python as a wrapper for third-party libraries -> numpy, scipy.

#  multiprocessing:
from multiprocessing import Process
import os

def square_numbers():
    for i in range(100):
        i * i

processes = []
num_processes = os.cpu_count()


# create processes
for i in range(num_processes):
    p = Process(target= square_numbers)  #if the function in the target has parameters, you have to pass args argument in the Processes and the data (the value) should be in a tuple.
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print("Ended Processing")

# Threads
from threading import Thread
import os

def square_numbers2():
    for i in range(100):
        i * i

threads = []
num_threads = 10


# create processes
for i in range(num_processes):
    t = Thread(target= square_numbers)  #if the function in the target has parameters, you have to pass args argument in the Processes and the data (the value) should be in a tuple.
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print("ended threads")