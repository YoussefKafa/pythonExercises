"""
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha=set()
        for i in sentence:
            if i in alpha:
                continue
            else:
                alpha.add(i)
        if len(alpha)==26:
            return True
        else:
            return False