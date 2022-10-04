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
#now lets learn how to create a new file and write on it

with open('test3.txt','w') as file:
    file.write("firstLine ")
    file.write("continue FirstLine")
    file.write("\n secondLine")
#as we can see that write() function writes on the same line,
#also everytime we execute the code , the file is replaced
#let's write multiple lines with a single line of code

with open('test4', 'w') as file:
    file.writelines(["first line", "\nsecond line", "\nthird line"])

#the file is replaced everytime we run the script, let's write to it without replacing it by using the append mode

with open('test4','a') as file:
    file.writelines(["\nfourth line"])

#Now let's read the whole file with read mode

with open('test4', 'r') as file:
    print(file.read()) #outputs the full file

#let's read only the first 10 characters

with open('test4','r') as file:
    print(file.read(10)) #outputs only the first 10 characters

#now let's read it line by line by using the readlines() function which returns a list of lines
with open('test4','r') as file:
    print(file.readlines()) #outputs a list of file lines that you can iterate over

