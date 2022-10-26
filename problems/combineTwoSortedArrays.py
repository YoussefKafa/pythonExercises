"""
Given two sorted integer arrays, return an array that combines both of them and is also sorted.
We can build the answer array ans one element at a time.
 Start two pointers at the first index of each array, and compare their elements. 
 At each iteration, we have 2 values.
  Whichever value is lower needs to come first in the answer, so add it to the answer and move the respective pointer.

"""

def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans

if __name__=='__main__':
    print(combine([1,2,3],[3,4,5]))