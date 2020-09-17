# the collections modules provides a special container data types and provides an alternative with some additional functionality.
# types of collections: Counter, namedtuple, orderedDict, defaultdict, deque.

# Counter:
# first import it ->

from collections import Counter

# its a container that stores elements as dict keys and their counts as their values

a = "aaaaaabbbbbbcccccc"
a_counter = Counter(a)
print(a_counter)
