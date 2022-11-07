def prefixSum(nums):
    prefix=[nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix

#calculating prefix sum in place
def runningSumOf1DArr(nums):
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    return nums

if __name__=='__main__':
    print(prefixSum([1,2,3,4,5,6]))
    print(runningSumOf1DArr([1,2,3,4,5,6]))