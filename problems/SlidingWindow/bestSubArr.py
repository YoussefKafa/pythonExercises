"""
Two pointers, Sliding window, fixed size window problem.
Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.
"""
def find_best_sub_arr(nums,k):
    curr=0
    for i in range(k):
        curr+=nums[i]
    ans=curr
    for i in range(k, len(nums)):
        curr+=nums[i] - nums[i-k]
        ans=max(curr,ans)
    return ans

print(find_best_sub_arr([1,2,3,4,5,6],1))
print(find_best_sub_arr([1,2,3,4,5,6],2))
print(find_best_sub_arr([3,-1,4,12,-8,5,6],4))