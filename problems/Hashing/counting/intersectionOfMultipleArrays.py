"""
Given a 2D array nums that contains n arrays of distinct integers,
 return a sorted array containing all the numbers that appear in all n arrays.
For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4].
 3 and 4 are the only numbers that are in all arrays.

"""
from collections import defaultdict
def intersection(arr:list[int])-> list[int]:
    counts=defaultdict(int)
    ans=[]
    for item in arr:
        for subItem in item:
            counts[subItem]+=1
    for k,v in counts.items():
        if v == len(arr):
            ans.append(k)
    return ans

if __name__=='__main__':
    print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))