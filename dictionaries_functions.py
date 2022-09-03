dic1={1:'coffe',2:'tea'}
print(dic1[1])
#coffe
dic1[1]="milk"
#milk
del dic1[1]
# {2: 'tea'}
dic2={1:'coffer',1:'tea',1:'milk'}
print(dic2)
# {1:'milk'}
del dic2[1]
#{}
dic2={1:'coffe', 2:'tea'}
for k in dic2:
    print(k)
#prints the keys 1 2 
for k,v in dic2.items():
    print(k)
    print(v)
# 1 coffe 2 tea
for v in dic2.values():
    print (v)
#coffe tea