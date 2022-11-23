"""
Given a string s, determine if all characters have the same frequency.
For example, given s = "abacbc", return true. All characters appear twice.
 Given s = "aaabb", return false.
 "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""
from collections import defaultdict
from collections import Counter
def equalFrequency(s:str) -> bool:
    counts=defaultdict(int)
    for c in s :
        counts[c]+=1
    frequencies=counts.values()
    return len(set(frequencies))==1


#one line solution
def areOccurrencesEqual(self, s: str) -> bool:
    return len(set(Counter(s).values())) == 1

if __name__=='__main__':
    print(equalFrequency("abacbc"))
    print(equalFrequency("aaabb"))