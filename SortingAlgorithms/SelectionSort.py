def selectionSort(nums:list[int]) -> list[int]:
    for i in range(len(nums)):
        minIndex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minIndex]:
                minIndex=j
        nums[i],nums[minIndex]=nums[minIndex],nums[i]
    return nums

if __name__=='__main__':
    nums=[10,9,8,7,6,5,4,3,2,1]
    print(selectionSort(nums))