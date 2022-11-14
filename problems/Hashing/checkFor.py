
"""
Given an integer array nums,
find all the numbers x that satisfy the following: x + 1 is not in nums,
and x - 1 is not in nums.
"""
def find_numbers(nums):
    ans = []
    nums = set(nums)
    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    return ans

"""
Very straightforward problem - we can just iterate through nums and check if x + 1 or x - 1 is in nums. By converting nums into a set beforehand, these checks are O(1)
Because the checks are O(1)  the time complexity is O(n)  since each for loop iteration runs in constant time. The set will occupy O(n)  space.
Anytime you find your algorithm running if ... in ..., then consider using a hash map or set to store elements to have these operations run in  O(1). Try these upcoming practice problems with what was learned here.
"""