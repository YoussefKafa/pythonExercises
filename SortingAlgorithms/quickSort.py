from random import randint
def quickSort(nums:list[int])-> list[int]:
    if len(nums)<=1:
        return nums
    pivot = nums[len(nums)//2]
    left= [x for x in nums if x<pivot]
    middle=[x for x in nums if x==pivot]
    right=[x for x in nums if x>pivot]
    return quickSort(left)+middle+quickSort(right)

#let's select the last element as the pivot
def quickSort2(nums:list[int])-> list[int]:
    if len(nums)<=1:
        return nums
    pivot = nums[-1]
    left= [x for x in nums[:-1] if x<pivot]
    middle=[x for x in nums if x==pivot]
    right=[x for x in nums[:-1] if x>pivot]
    return quickSort(left)+middle+quickSort(right)

#let's select the first element as the pivot
def quickSort3(nums:list[int])-> list[int]:
    if len(nums)<=1:
        return nums
    pivot = nums[0]
    left= [x for x in nums[1:] if x<pivot]
    middle=[x for x in nums if x==pivot]
    right=[x for x in nums[1:] if x>pivot]
    return quickSort(left)+middle+quickSort(right)

#let's select a random element as the pivot
def quickSort4(nums):
    if len(nums) <= 1:
        return nums
    left,middle,right=[],[],[]
    pivot=nums[randint(0,len(nums)-1)]
    for i in nums:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            middle.append(i)
        else:
            right.append(i)
    return quickSort4(left)+middle+quickSort4(right)


if __name__ == '__main__':
    nums=[10,9,8,7,6,5,4,3,2,1]
    sorted=quickSort(nums)
    print(sorted)
    nums=[10,9,8,7,6,5,4,3,2,1]
    sorted=quickSort2(nums)
    print(sorted)
    nums=[10,9,8,7,6,5,4,3,2,1]
    sorted=quickSort3(nums)
    print(sorted)
    nums=[10,9,8,7,6,5,4,3,2,1]
    sorted=quickSort4(nums)
    print(sorted)