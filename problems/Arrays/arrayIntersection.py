"""

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    dict={}
    result=[]
    for i in nums1:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for i in nums2:
        if i not in dict:
            continue
        else:
            result.append(i)
            dict[i]-=1
            if dict[i]==0:
                del dict[i]
    return result
print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))
print([2]*5)


def findTheIntersectionOfTwoArrays(num1:list, num2:list) -> list:
    i,j=0,0
    res=[]
    num1.sort()
    num2.sort()
    while i<len(num1) and j<len(num2):
        if num1[i]==num2[j]:
            res.append(num1[i])
            i+=1
            j+=1
        elif num1[i]<num2[j]:
            i+=1
        else:
            j+=1
    return res