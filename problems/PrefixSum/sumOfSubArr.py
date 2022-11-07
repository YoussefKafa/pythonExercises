from prefixSum import prefixSum
"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
the prefix sum array is :
[1,7,10,12,19,21]
prefix[3]-prefix[0]+nums[0]
12-1 + 1 = 12 -> true
prefix[5]-prefix[2] + nums[2]
11 + 3= 14 -> true
prefix[4] - prefix[2] + num[2]
19-10 + 3 = 12 -> true
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
the prefix sum array is :
[1,7,10,12,19,21]
prefix[3]-prefix[0]+nums[0]
12-1 + 1 = 12 -> true
prefix[5]-prefix[2] + nums[2]
11 + 3= 14 -> true
prefix[4] - prefix[2] + num[2]
19-10 + 3 = 12 -> true
"""
def answer_queries(nums,queries,limit):
    prefix=prefixSum(nums)
    ans=[]
    for x,y in queries:
        curr=prefix[y]-prefix[x]+nums[x]
        ans.append(curr<limit)
    return ans


if __name__=='__main__':
    print(answer_queries([1, 6, 3, 2, 7, 2],[[0, 3], [2, 5], [2, 4]],13))