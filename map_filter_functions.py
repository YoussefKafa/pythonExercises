"""
Maps take all objects in a list and applies a function
Filters do the same , but take the results and creates a new list with only the true values
consider this example:
We have a list of names and we want to get only the names that starts with the letter a.
"""

#first we create the function that checks if the name starts with the letter a
list_of_names=["aaya", "youssef","john", "ahmad"]
def check_name(name):
    if name.startswith('a'):
        return name

#now lets use the map() function to check the names, it will take two arguments, the function itself, and the list

result=map(check_name,list_of_names)
print(result)
#prints <map object at 0x000001DB46F5AD70>
for x in result:
    print(x)
"""
prints:
aaya
None
None
ahmad
"""

#now lets use the filter() function instead

result=filter(check_name,list_of_names)
print(result)
#prints <filter object at 0x00000250DBBABBB0>
for x in result:
    print(x)
"""
prints:
aaya
ahmad
"""