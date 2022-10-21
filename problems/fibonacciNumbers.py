import sys
print(sys.argv[0]) #prints the file name
arg=int(sys.argv[1])
def fibonacciNumbersTo(n):
        if n<=1:
            return n
        oneBack=fibonacciNumbersTo(n-1)
        twoBack=fibonacciNumbersTo(n-2)
        return oneBack+twoBack

if __name__=='__main__':
    print(fibonacciNumbersTo(arg))

"""
divide the original problem into subproblems and then combine the subproblems solutions to get the original problem solution
oneBack = F(2)
    oneBack = F(1)
        F(1) = 1
    twoBack = F(0)
        F(0) = 0
    F(2) = 0 + 1 = 1
twoBack = F(1)
    F(1) = 1
oneBack + twoBack = 2
"""