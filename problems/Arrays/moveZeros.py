"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""


def moveZeroes(nums:list[int]) -> list[int]:
    for i in nums:
        if i==0:
            nums.remove(i)
            nums.append(i)

def moveZeroes1(nums:list[int])->list[int]:
    left=0
    for i in range(len(nums)):
        if nums[i]:
            nums[left],nums[i]=nums[i],nums[left]
            left+=1
    return nums

print(moveZeroes1([1,2,3]))
"""
Initial state:
nums = [0, 1, 0, 2]
left = 0

Iteration 1 (i = 0):
- nums[i] = 0, so the if statement is not executed
- The state of nums and left remains unchanged

Iteration 2 (i = 1):
- nums[i] = 1, so the if statement is executed
- nums[left] and nums[i] are swapped, resulting in nums = [1, 0, 0, 2] and left = 1

Iteration 3 (i = 2):
- nums[i] = 0, so the if statement is not executed
- The state of nums and left remains unchanged

Iteration 4 (i = 3):
- nums[i] = 2, so the if statement is executed
- nums[left] and nums[i] are swapped, resulting in nums = [1, 2, 0, 0] and left = 2

The loop terminates because all indices of nums have been processed. The resulting list is [1, 2, 0, 0], which has all the zeros at the end of the list in their original order.

Final state:
nums = [1, 2, 0, 0]
left = 2

The function returns [1, 2, 0, 0].

"""