"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 
"""

def rotate(nums:list[int],k:int):
    while k > 0:
        num=nums.pop()
        nums.insert(0,num)
        k = k - 1
def rotate2(nums:list[int],k:int):
        l = len(nums) # 4
        k = k%l # 4%2 =0
        nums[0:l] = nums[l-k:l] + nums[0:l-k]
nums=[-1,-100,3,99]
rotate(nums,2)
print(nums)
nums=[-1,-100,3,99]
rotate2(nums,2)
print(nums)