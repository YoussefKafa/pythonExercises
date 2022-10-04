def sum(a,b):
    return a+b
print(sum(1,2)) #3

def sum1(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum1(1,2,3)) #6

