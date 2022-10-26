"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""
def sortedSquares( nums: list[int]) -> list[int]:
    i=0
    while i < len(nums):
        nums[i]=pow(nums[i],2)
        i+=1
    return(sorted(nums))
if __name__=='__main__':
    print(sortedSquares([-4,-1,0,3,10]))