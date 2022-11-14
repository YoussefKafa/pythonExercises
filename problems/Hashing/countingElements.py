"""
Given an integer array arr, count how many elements x there are, 
such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
"""
def countElements(arr: list[int]) -> int:
    counter=0
    for i in arr:
        if (i+1) in arr:
            counter+=1
    return counter

#Use set to check in O(1), so the faster solution is

def countElements1(arr:list[int])->int:
    counter=0
    numSet=set(arr)
    for num in arr:
        if num+1 in numSet:
            counter+=1
    return counter
print(countElements([1,2,3]))
print(countElements([1,1,3,3,5,5,7,7]))
print(countElements1([1,2,3]))
print(countElements1([1,1,3,3,5,5,7,7]))