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