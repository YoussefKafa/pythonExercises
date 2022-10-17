class Solution:
    def search(self,nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0
        while low <= high:
            mid=(high+low)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                return mid
        return -1
if __name__ == '__main__':
    nums=[-1,0,3,5,9,12]
    target=9
    sol=Solution()
    print(sol.search(nums,target))