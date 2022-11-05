"""
Two Pointers, Sliding window, fixed size window problem.
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
"""
def findMaxAverage(nums:list[int],k:int)->float:
    curr=0
    for i in range(k):
        curr+=nums[i]
    ans=curr/k
    for i in range(k, len(nums)):
        curr+= nums[i] - nums[i-k]
        ans=max(ans, curr/k)
    return ans

print(findMaxAverage([1,2,3,4,5],2)) # the answer is (4+5)/2=4.5