

def bubbleSort(nums:list[int])->list[int]:
    swapped=False
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                swapped=True
                nums[j],nums[j+1]=nums[j+1],nums[j]
        if not swapped:
            break
def reversedBubbleSort(nums:list[int])->list[int]:
    swapped=False
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]<nums[j+1]:
                swapped=True
                nums[j],nums[j+1]=nums[j+1],nums[j]
        if not swapped:
            break
if __name__ == '__main__':
    nums=[10,9,8,7,6,5,4,3,2,1]
    bubbleSort(nums)
    print(nums)
    nums=[10,9,8,7,6,5,4,3,2,1]
    reversedBubbleSort(nums)
    print(nums)