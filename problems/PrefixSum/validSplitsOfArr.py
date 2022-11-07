"""
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
A brute force approach would be to iterate over each index i from 0 until nums.length - 1. For each index, iterate from 0 to i to find the sum of the left section, and then iterate from i + 1 until the end of the array to find the sum of the right section. This algorithm would have a time complexity of O(n^2).
If we build a prefix sum first, then iterate over each index, we can calculate the sums of the left and right sections in O(1), which would improve the time complexity to O(n).
example:
the original array is:
[10,4,-8,7]
the prefix sum array is:
[10,14,6,13]
first split:
[10] [4,-8,7] , 10 >= 13-10 , True
second split:
[10,4] [-8,7] , 14 >= 13-14 , True
third split:
[10,4,-8] [7] , 6 >= 13-6 , False
"""
from prefixSum import prefixSum
def validSPlitsOfArr(nums):
    prefix=prefixSum(nums)
    ans=0
    for i in range(len(nums)-1):
        left=prefix[i]
        right=prefix[-1] - prefix[i]
        if left >= right:
            ans+=1
    return ans
        
if __name__ == '__main__':
    print(validSPlitsOfArr([10,4,-8,7]))