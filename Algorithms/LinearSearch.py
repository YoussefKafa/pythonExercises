#also called brute force
class Solution:
    @staticmethod
    def findKthPositive(arr: list[int], k: int) -> int:
        # if the kth missing is less than arr[0]
        """
        example: [3,4,5] 2
        2 <= 2
        return 2
        """
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1
        print('initial k: ',k)

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):
            # missing between arr[i] and arr[i + 1]
            curr_missing = arr[i + 1] - arr[i] - 1
            print('curr_missing :',arr[i+1] , ' - ', arr[i]-1,curr_missing)
            # if the kth missing is between
            # arr[i] and arr[i + 1] -> return it
            if k <= curr_missing:
                print('k <= curr_missing we should return : ',' arr[i]+k ' , arr[i], ' + ' , k , arr[i]+k)
                return arr[i] + k
            # otherwise, proceed further
            k -= curr_missing

        # if the missing number if greater than arr[-1]
        return arr[-1] + k

if __name__ == '__main__':
    print(Solution.findKthPositive([3,4,5],6))