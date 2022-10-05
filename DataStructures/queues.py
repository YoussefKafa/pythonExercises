# first implementation

queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
#print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
#print(queue)



#second way of implementation using queue.deque
from collections import deque
from sys import maxsize
queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
#print(queue) #outputs deque([1,2,3])
queue.popleft()
queue.popleft()
#print(queue) #outputs deque([3])
queue.popleft()
#print(queue) #outputs deque([])




#third way of implementing a queue in python using the Queue module

from queue import Empty, Queue
queue=Queue(maxsize=3)
queue.put(1)
queue.put(2)
queue.put(3)
#print(list(queue.queue))
queue.get()
queue.get()
#print(queue.full()) #not full so it will print False
#print(list(queue.queue))
queue.get()
#print(list(queue.queue))

