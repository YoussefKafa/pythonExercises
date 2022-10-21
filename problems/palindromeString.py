import sys

def isPalindrome(s):
    left=0
    right=len(s)-1
    l=list(s)
    while left<right:
        if l[left]!=l[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == '__main__':
    print(isPalindrome(sys.argv[1]))