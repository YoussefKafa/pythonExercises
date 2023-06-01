def insertionSort(nums:list[int])->list[int]:
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

if __name__=='__main__':
    nums=[10,9,8,7,6,5,4,3,2,1]
    print(insertionSort(nums))