def binarySearch(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
def recursiveBinarySearch(nums,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return recursiveBinarySearch(nums,target,mid+1,high)
    else:
        return recursiveBinarySearch(nums,target,low,mid-1)
if __name__=='__main__':
    nums=[1,2,3,4,5,6,7,8,9]
    target=8
    print(binarySearch(nums,target))
    print(recursiveBinarySearch(nums,target,0,len(nums)-1))