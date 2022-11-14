class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
if __name__=='__main__':
    sol=Solution()
    print(sol.missingNumber([0,1]))
    print(sol.missingNumber([3,0,1]))
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))