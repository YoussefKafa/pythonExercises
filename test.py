def staircase(n):
    for i in range(1,n+1):
            str1=getChrs(' ',n-i)
            str2=getChrs('#',i)
            print(str1+str2)
def getChrs(chr,n):
    h=''
    for i in range(n):
        h+=chr
    return h
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)