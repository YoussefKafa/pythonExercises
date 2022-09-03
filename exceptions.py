def divide(a,b):
    return a/b

print(divide(2,2)) 
#outputs 1.0
#print(divide(2,0))
#outputs ZeroDivisionError: division by zero
#and terminate the execuation of the code



#let's solve that by handling the exception
def divide_right(a,b):
    try:
        return a/b
    except Exception as e:
        print("somthing went wrong")
        print(e.__class__)
        print(e.__doc__)
print(divide_right(2,0))
#outputs the following:
# something went wrong
# <class 'ZeroDivisionError'>
# Second argument to a division or modulo operation was zero.

#Like with any programming language exceptions happen in Python.
#You can handle more than one exception by chaining the except statement by adding another except statement.​ 
def divide_right_1(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("somthing went wrong")
        print(e.__class__)
        print(e.__doc__)
    except Exception as e:
        print(e)