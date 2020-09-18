# the collections modules provides a special container data types and provides an alternative with some additional functionality.
# types of collections: Counter, namedtuple, orderedDict, defaultdict, deque.

# Counter:
# first import it ->

from collections import Counter

# its a container that stores elements as dict keys and their counts as their values

a = "aaaaaaaaaaabbbbbbbbbccccccc" # we can use a list or any other iterable
a_counter = Counter(a)
print(a_counter)
print(a_counter.items())
print(a_counter.keys())
print(a_counter.values())


# to find the most common element in the counter dict
print(a_counter.most_common(1)) #1 is for the very first. use 2 for the 2 most common

# to look only at the most common element
print(a_counter.most_common(1)[0])

# to look only at the  element
print(a_counter.most_common(1)[0][0])

# to get the list of all the different elements and this will give us an iterable of elements repeating each many times as the count. convert it to a list to be seen nicely.
print(list(a_counter.elements()))

# namedtuple
# is an easy way to create an object type similar to a struct
# import fist

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
# ^ first define it then as a first argument will be the class name, typically it is same as the defi, and the second argument is a string with the fields wanted separated by a comma or a space

pt1 = Point( 1, -4)
print(pt1)
print(pt1.x, pt1.y)


# OrderedDict
# is a dict but remeber the order they where inserted
# import below

from collections import OrderedDict 

ordered_dict = OrderedDict()
ordered_dict['c'] = 4
ordered_dict['b'] = 9
ordered_dict['d'] = 6
ordered_dict['a'] = 1

print(ordered_dict)

# defaultdict
# similar to the usual dict but it will have a default vlaue if the key is not set.
# import below
from collections import defaultdict

d = defaultdict(int) # the argument will be the default type. int, float, list

d['q'] = 9
d['a'] = 5
d['s'] = 7
d['x'] = 3

print(d)
print(d['w'])


# deque
# its a double ended que. it can be used to add or remove elements from both ends and both are efficient

# first import it

from collections import deque

dd = deque()

dd.append(1)
dd.append(2)
dd.append(5)
dd.append(8)

print(dd)

dd.appendleft(9)
print(dd)

dd.pop()
print(dd)

dd.popleft()
print(dd)

dd.extend([99,33,77])
print(dd)

dd.extendleft([88,44,22])
print(dd)

dd.rotate(1) #can use a negative value
print(dd)

dd.clear()
print(dd)