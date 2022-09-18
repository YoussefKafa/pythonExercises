def count(times):
    for i in range(1,times+1):
        yield i
if __name__=='__main__':
   for x in count(10):
    print(x)