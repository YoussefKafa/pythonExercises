"""
it is an array or a list , it is a linear data structure that stores items
in a last-in/first-out or first-in/last-out manner.
in stacks , a new element is added to one end and an element is removed from that end only.
the insert and delete operations are often called push and pop.
"""

#implementation using lists
#LIFO
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
#print(stack)
stack.pop()
stack.pop()
#print(stack)

#####################################################################

# Implementation using collections.deque:
# LIFO
from collections import deque

stack=deque()
stack.append(1)
stack.append(2)
stack.append(3)
#print(stack) #deque([1,2,3])
stack.pop()
stack.pop()
#print(stack) # deque([1])