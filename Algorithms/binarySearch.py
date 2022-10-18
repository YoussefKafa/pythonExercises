class Solution:
    def search(self,nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0
        while low <= high:
            mid=(high+low)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                return mid
        return -1
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
"""
def firstBadVersion(self, n: int) -> int:
    if n==1 : return 1
    left=1
    right=n
    while left<right:
        mid=int(left+(right-left)/2)
        if isBadVersion(mid):
            right=mid
        else:
            left=mid+1
    return left
"""
if __name__ == '__main__':
    nums=[-1,0,3,5,9,12]
    target=9
    sol=Solution()
    print(sol.search(nums,target))