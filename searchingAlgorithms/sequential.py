def sequencialSearch(nums:list[int],target:int)-> list[int]:
    for i,v in enumerate(nums):
        if v==target:
            return i
    return -1

if __name__=='__main__':
    nums=[10,9,8,7,6,5,4,3,2,1]
    print(sequencialSearch(nums,5))
    print(sequencialSearch(nums,11))