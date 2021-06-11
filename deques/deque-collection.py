import collections
from collections import deque

d = deque("hello")
print(d)

d.appendleft("d")
d.extend([1,2,3,4,5])
print(d)
d.extendleft("xyz")
d.rotate(-3)
print(d)
d.reverse()
print(d)

deck = deque("maxim", 5)
print(deck)
deck.append("l")
print(deck)