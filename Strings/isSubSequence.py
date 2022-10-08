
# solution using pointers
class Solution:
    # the functions takes two strings: the source and the target , and returns boolean
    def isSubSequence(self, s: str, t:str) -> bool:
        #we define the sizes
        sourceSize, targetSize=len(s),len(t)
        #we define two pointers, one for the left string , and one for the right string
        pLeft=pRight=0
        # while we haven't reached the end of the two strings
        while pLeft<sourceSize and pRight<targetSize:
            # if the two characters are equal then we move forward in the source string
            if s[pLeft] == t[pRight]:
                pLeft+=1
            # if they are not equal , then we move forward in the target string to check another char
            pRight+=1
        #if the left pointer is equal to the source string length, then we've just found that
        # the source string is a subsequence of the target string
        return pLeft==sourceSize

if __name__ == '__main__':
    sol=Solution()
    print(sol.isSubSequence("abc","axxbxxcxx"))
    print(sol.isSubSequence("abc","axxcxxbxx"))