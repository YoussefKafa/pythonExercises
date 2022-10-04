set1={1,2,3,4,5}
set1={1,1,2,3,4,5,5}
#output {1,2,3,4,5}
set1={1,2,1,3,4}
#output {1,2,3,4}
#print(set1[0])
#output ERROR TypeError: 'set' object is not subscriptable
set1.add(6)
#output {1,2,3,4,6}
set1.remove(6)
#or
set1.discard(6)
set1={4,2,3,1,4}
set2={7,5,6}
print(set1.union(set2))
#or
print(set1 | set2)
#output {1,2,3,4,5,6,7}
set1={1,2,"s"}
set2={3,"b"}
print(set1 | set2)
#output {1,2,3,'b','s'}
#set1={1,2,[3,4]}
#ERROR TypeError: unhashable type: 'list'
set1={1,2,3}
set2={1,3}
print(set1.intersection(set2))
print(set1 & set2)
#output {1,3}
set1={1,2}
set2={3,4}
print(set1 & set2)
#output set()
print(set1.difference(set2)) #in set1 but not in set2
print(set1 - set2)
#output {1,2}
print(set1.symmetric_difference(set2)) #in set1 or in set2 but not in both
print(set1 ^ set2) #caret operator
#output {1,2,3,4}
set1={1,2,3}
for i in set1:
    print(i)