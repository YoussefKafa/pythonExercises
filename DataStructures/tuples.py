from filecmp import cmp


tuple1=(1,"str",2.0,1,True)
print(tuple1[1]) #str
#tuple1[0]=2 #ERROR because tuples are immutable
#tuple has not insert,append, extend,pop,clear,remove,reverse,sort,copy functions because its immutable
#tuple functions are : index , count, len
print(tuple1.index("str")) #1
print(tuple1.count(1)) #3 because True is also 1
tuple2=(1,2,3)
print ( max(tuple2) )
print ( min(tuple2) )
