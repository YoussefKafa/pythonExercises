"""
Given an array of integers nums and an integer target,
return indices of two numbers such that they add up to target.
You cannot use the same index twice.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            dic[num] = i      
        return [-1, -1]


