#if we have a list
myList=[1,2,3]
resultOfSum=(lambda x:sum(x))(myList)

right=1
result= (lambda x:1 if right else 0)(right)

#generating a list
n=2
powList=[lambda arg=x: arg**n for x in range(0,10)]
for x in powList:
    pass
    #print(x())

#generating a list
f=lambda x:x**2
powList=[f(i) for i in range(10)]
print(powList)

#lambda functions
maximumValue = lambda a,b : a if a>b else b
#print(maximumValue(10,100))

