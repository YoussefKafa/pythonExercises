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




