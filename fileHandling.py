"""
file handling functions are open() and close()
let's try to work with open() function
the open function accepts two arguments open(<file_name_or_location>,<mode>)
modes are :
 r for open and read in a text format
 r+ open for reading and writing
 w open for writing
a for editing and appending
 add b for any mode to work with the file in a binary format
close() function to close the file
we can forget about the close() function if we use the 'with' keyword i.e : with open .. as we will see in the exercise
"""
#exercise 1

file = open('test1.txt',mode='r')
firstLine=file.readline()
secondLine=file.readline()
print(firstLine) #prints hello world! 
print(secondLine) #prints bye world!
file.close() #close the file
file = open('test1.txt',mode='r') #open it again so we can learn how to read all lines at once
lines=file.readlines()
for line in lines:
    print(line)
    """
prints:
hello world!
bye world!
    """
file.close() #always remember to close the file if you don't use the 'with' keyword, or let's use it

with open('test2.txt',mode='r') as file:
    print(file.readlines())
#prints ['hello\n', 'there!'] because we didn't iterate over the list of lines 

with open('test2.txt',mode='r') as file:
    for line in file.readlines():
        print(line)
"""
prints:
hello
there!
"""
