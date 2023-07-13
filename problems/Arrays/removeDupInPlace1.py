def remove_duplicates(nums):
    # Check if the array is empty or has only one element
    print(len(nums))
    if len(nums) < 2:
        return

    # Sort the array (optional, but simplifies the algorithm)
    nums.sort()

    # Initialize two pointers: one for the current element and one for the next distinct element
    i = 0
    j = 1

    # Iterate through the array
    while j < len(nums):
        # If the current element is equal to the next distinct element, move the next distinct pointer forward
        if nums[i] == nums[j]:
            j += 1
        # If the current element is different from the next distinct element, update the array and pointers
        else:
            i += 1
            nums[i] = nums[j]
            j += 1

    # Truncate the array after the last distinct element
    del nums[i+1:]


arr=[1,3,3,2,2]
"""
i=0
j=1
sort the array : [1,2,2,3,3]
j<len(nums) -> 1<5 -> True
nums[i]=nums[j] -> 1=2 -> False
i+=1 -> i=1
nums[i]=nums[j] -> [1,2,2,3,3]
j+=1 -> j=2
___
i=1 , j=2 , j<len(nums) -> true
nums[i]==nums[j] ? -> 2==2 -> True
j+=1 -> j=3
____
i=1 , j=3 , j<len(nums) -> true
nums[i]==nums[j] ? -> 2==3 -> False
i+=1 -> i=2
nums[i]=nums[j] -> [1,2,3,3,3]
j+=1 -> j=4
__
i=2 , j=4 , j<len(nums) -> true
nums[i]==nums[j] ? -> 3==3 -> True
j+=1 -> j=5
___
i=2 , j=5 , j<len(nums) -> false -> break 
delete [i+1:] to stay with [1,2,3]
"""
remove_duplicates(arr)
print(arr)