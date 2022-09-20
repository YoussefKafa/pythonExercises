#the extended slice syntax is [start:stop:step], start index is included but stop index is not
str="python"
#print(str[1:2]) # items from index 1 through index 2
#output y
print(str[:2]) #items from index 0 through 2
#output py
print(str[:-2])
#output pyth
print(str[::2])
#output pto
print(str[::-1]) #reverse
#output nohtyp
print(str[:])
#output python
name='youssef'
#print("Hey, %s!" % name) 
#prints Hey, youssef!
first='youssef'
last='kafa'
#print("Hey, %s %s!" %(first,last))
#prints Hey, youssef kafa!
#print("x",2,"y",3,"z") #prints x 2 y 3 z (space between)
#print('%d' %('youssef')) #error a real number is required
#print('%d' %(20.00)) #prints 20
