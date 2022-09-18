def count(times):
    for i in range(1,times+1):
        yield i
if __name__=='__main__':
   for x in count(10):
    print(x)

"""
yield : Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator.
"""