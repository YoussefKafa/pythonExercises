"""
The string is called isomorphic
if the letters of the one string can be mapped to get the second string. 
Mapping means replacing all occurrences of a letter with another letter
but the ordering of the letters remains unchanged.
Note that no two letters may map to the same letter but a letter may map to itself.
"""
# Definition for singly-linked list.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaceWith={}
        if len(s)==0 or len(s)==1:
            return True
        pointer=0
        resultString=""
        while pointer < len(s):
            if s[pointer] in replaceWith or t[pointer] in replaceWith.values():
                pass
            else:
                replaceWith[s[pointer]]=t[pointer]
            pointer+=1
        for i in range(len(s)):
            if s[i] in replaceWith:
                resultString+=replaceWith[s[i]]
            else:
                return False
        return resultString==t
if __name__ == '__main__':
    sol=Solution()
    print(sol.isIsomorphic("egg","add"))
    print(sol.isIsomorphic("badc","baba"))