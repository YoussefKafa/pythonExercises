"""
Given a string s, return the first character to appear twice.
It is guaranteed that the input will have a duplicate character.
"""

class Solution:
    """
    This is O(n^2) due to the nested loop. The second loop is checking for the existence of c, which can be done in O(1) using a set.
    """
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c

        return ""
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return " "
    """
    This improves our time complexity to O(n) as each for loop iteration now runs in constant time. The set will also occupy O(n)O(n) space.
    """