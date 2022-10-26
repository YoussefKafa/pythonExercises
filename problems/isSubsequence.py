"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
We can use two pointers to solve this in linear time. If we find that s[i] == t[j], that means we "found" the letter at position i for s, and we can move on to the next one by incrementing i. We should increment j at each iteration (which means we could also implement this algorithm using a for loop). s is a subsequence of t if we can "find" all the letters of s, which means that i == s.length at the end of the algorithm.

"""
def isSubsequence( s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


if __name__ == '__main__':
    print(isSubsequence('kafa','akbawfwa'))