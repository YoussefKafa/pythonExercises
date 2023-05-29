"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
# We can use the two pointers method to solve this problem. The idea is to have one pointer for iterating the array and another pointer that only moves when we find a new unique element. The second pointer will be the one that will be used to overwrite the array with the unique elements.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:      
                nums[insertIndex] = nums[i] 
                insertIndex = insertIndex + 1    
        print(nums)   
        return insertIndex
sol=Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([1,1,2,3]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

"""
Time Complexity: O(n)
Space Complexity: O(1)
EXAMPLE:
[1,1,2]
size=3
insertIndex=1
i=1 -> nums[0]=1, nums[1]=1 -> insertIndex=1
i=2 -> nums[1]=1, nums[2]=2 -> nums[1]=2, insertIndex=2
i=3 -> i>size -> return insertIndex=2
"""