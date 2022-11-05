"""
Given an array of positive integers nums and an integer k,
return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
For example, 
given the input nums = [10, 5, 2, 6], k = 100, 
the answer is 8. The subarrays with products less than k are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

def numSubarrayProductLessThanK(nums:list[int],k:int)-> int:
    left=ans=0
    curr=1
    for right in range(len(nums)):
        curr*=nums[right]
        while left<=right and curr>=k:
            curr//=nums[left] #this is how we roll back a product
            left+=1
        ans+=right-left+1
    return ans

print(numSubarrayProductLessThanK([10,5,2,6],100))
print(numSubarrayProductLessThanK([1,1,1,1,0],100))
print(numSubarrayProductLessThanK([20,20,20],100))
print(numSubarrayProductLessThanK([1000],100))