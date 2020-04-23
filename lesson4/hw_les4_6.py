from itertools import count
for i in count(9, 10):
    print(i)

from itertools import cycle
a = [5, 6, 7, 8, 9]
for i in cycle(a):
    print(i)