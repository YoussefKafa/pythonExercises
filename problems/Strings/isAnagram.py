"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
def isAnagram(s: str, t: str) -> bool:
    return sorted(s)==sorted(t)

def isAnagram1(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in t:
        if i in count:
            count[i]-=1
        else:
            count[i]=1
    for i in count:
        if count[i]!=0:
            return False
    return True

def isAnagram2(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    