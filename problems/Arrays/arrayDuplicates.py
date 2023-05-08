"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(nums: list[int]) -> bool:
    values={}
    for i in nums:
        if i in values:
            values[i]+=1
        else:
            values[i]=1
    for i,k in values.items():
        print(i,k)
        if k>1:
            return True
    return False



def containsDuplicate2(nums: list[int]) -> bool:
        values={}
        for i in nums:
            if i in values:
                return True
            else:
                values[i]=1
        return False
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate2([1,2,3,1]))