def minStartValue( nums: list[int]) -> int:
    counter=1
    while True:
        ans=[counter+nums[0]]
        for i in range(1,len(nums)):
            ans.append(ans[-1]+nums[i])
        if min(ans)>=1:
            return counter
        else:
            counter+=1

if __name__=='__main__':
    print(minStartValue([-3,2,-3,4,2]))
    print(minStartValue([1,2]))
    print(minStartValue([1,-2,-3]))