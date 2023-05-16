"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverseString(str:list[chr]) -> list[chr]:
    for i in range(len(str)-1):
        str.insert(i,str.pop())
    return str
def reverseString1(str:list[chr]) -> list[chr]:
    str.reverse()
    return str

def reverseString2(str:list[chr]) -> list[chr]:
    print("string length: ",len(str))
    print("starting from 0 to ",len(str)//2)
    for i in range(len(str)//2):
        print("i: ",i)
        print("str[i]: ",str[i])
        print("str[len(str)-i-1]: or str[ ",len(str)-i-1,"] ",str[len(str)-i-1])
        print("swapping: ",str[i]," and ",str[len(str)-i-1])
        str[i],str[len(str)-i-1]=str[len(str)-i-1],str[i]
        
    return str

def reverseString3(str:list[chr])->list[chr]:
    str[:]=str[::-1]
    return str
"""
['h','e','l','l','o'] = reverseString
i=0
str[0],str[]
"""
if __name__=='__main__':
    str=["h","e","l","l","o"]
    print(reverseString(str))
    str=["h","e","l","l","o"]
    print(reverseString1(str))
    str=["h","e","l","l","o"]
    print(reverseString2(str))
    str=["h","e","l","l","o"]
    print(reverseString3(str))