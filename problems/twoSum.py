"""
Given a sorted array of unique integers and a target integer,
return true if there exists a pair of numbers that sum to target
"""
def twoSum(lista,target):
    left=0
    right=len(lista)-1
    while left<right:
        curr=lista[left]+lista[right]
        if curr==target:
            return True
        elif curr>target:
            right-=1
        elif curr<target:
            left+=1
    return False
if __name__=='__main__':
    print(twoSum([1,2,3,4,10,12],20))