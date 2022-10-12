list1=[1,'A',True,2.0, [1,2,3]]
print(*list1)
#prints the full list
#output: 1 A True 2.0 [1, 2, 3]
print(list1, sep=" ")
print(list1, sep=",")
#output [1, 'A', True, 2.0, [1, 2, 3]]
list2=[1,2]
list2.insert(len(list2),3)
#output [1,2,3] when list2 is printed
list2.insert(0,0)
#output [0,1,2,3] when list2 is printed
list2.append(4)
#output [0,1,2,3,4] when list2 is printed
list2.extend([5,6])
#output [0,1,2,3,4,5,6] when list2 is printed
list2.pop()
#output [0,1,2,3,4,5] when list2 is printed
list2.pop(0)
#or
del list2[0]
#output [1,2,3,4,5] when list2 is printed
list2.clear()
#output []  when list2 is printed
list2=[1,2,1]
list2.remove(1)
#output [2,1] when list2 is printed
#list2.remove(5)
#output ValueError: list.remove(x): x not in list
list2=[1,2,3,4]
print(list2.index(1))
#output 0
#print(list2.index(5))
#ValueError: 5 is not in list
#print(list2.index(1,1,3)) #search from index 1 to index 3
#ValueError: 5 is not in list
list2=[1,2,1]
print(list2.count(1))
#output 2
list2=[1,2,3]
list2.reverse()
#output [3,2,1]
print(list2.reverse()) 
#output None , you can not print it, but it did reverse the list
print(list2)
#output [1,2,3]
list2=[1,3,2]
#print(list2[::-1]) prints [2,3,1]
list2.sort()
#output [1,2,3]
list3=list2.copy()
#list3 output[1,2,3]
list3[0]=2
#list3[3]=4 IndexError: list assignment index out of range
#list3 output [2,2,3] Lists are mutable