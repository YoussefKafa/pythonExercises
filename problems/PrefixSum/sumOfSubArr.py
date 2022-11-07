from prefixSum import prefixSum

def answer_queries(nums,queries,limit):
    prefix=prefixSum(nums)
    ans=[]
    for x,y in queries:
        curr=prefix[y]-prefix[x]+nums[x]
        ans.append(curr<limit)
    return ans


if __name__=='__main__':
    print(answer_queries([1, 6, 3, 2, 7, 2],[[0, 3], [2, 5], [2, 4]],13))