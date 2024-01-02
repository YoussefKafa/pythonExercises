from random import randint
class Solution:
    # Defines a class named Solution.

    def sortArray(self, nums: list[int]) -> list[int]:
        # Defines a method 'sortArray' within the class, which takes a list of integers as input and returns a list of integers.

        def quick_sort(l, r):
            # Defines a nested function 'quick_sort' for sorting a part of the array. 
            # 'l' is the left index and 'r' is the right index of the sub-array to be sorted.

            if l >= r:
                return
                # Base case for the recursion. If the left index is greater than or equal to the right index,
                # the function returns, as there are no elements to sort.

            x = nums[randint(l, r)]
            # Selects a random pivot 'x' from the sub-array. This helps in optimizing the performance 
            # and avoiding worst-case scenarios in quicksort.

            i, j, k = l - 1, r + 1, l
            # Initializes three pointers: 
            # 'i' starts from one position left of the sub-array,
            # 'j' starts from one position right of the sub-array,
            # 'k' starts from the left index of the sub-array.

            while k < j:
                # Iterates as long as the 'k' pointer is less than the 'j' pointer.

                if nums[k] < x:
                    # If the current element is less than the pivot:
                    nums[i + 1], nums[k] = nums[k], nums[i + 1]
                    # Swap the current element with the element at 'i + 1' position.
                    i, k = i + 1, k + 1
                    # Move the 'i' and 'k' pointers one step forward.

                elif nums[k] > x:
                    # If the current element is greater than the pivot:
                    j -= 1
                    nums[j], nums[k] = nums[k], nums[j]
                    # Decrease the 'j' pointer and swap the current element with the element at 'j' position.

                else:
                    # If the current element is equal to the pivot:
                    k = k + 1
                    # Move the 'k' pointer one step forward.

            # At this point, all elements less than the pivot are to the left of 'i',
            # and all elements greater than the pivot are to the right of 'j'.

            quick_sort(l, i)
            # Recursively sort the left part of the sub-array.
            
            quick_sort(j, r)
            # Recursively sort the right part of the sub-array.

        # Start sorting the entire array.
        quick_sort(0, len(nums) - 1)

        return nums
        # Return the sorted array.

"""
Detailed Explanation
The class Solution contains the method sortArray, which takes nums as input and returns a sorted array.
"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Create a DP table with the same dimensions as the grid
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # If the starting cell has an obstacle, return 0 as no path is possible
        if obstacleGrid[0][0] == 1:
            return 0

        # Initialize the starting point
        dp[0][0] = 1

        # Fill the first column of the DP table
        for i in range(1, m):
            # A cell in the first column is reachable only if there is no obstacle 
            # and the cell above it is reachable
            dp[i][0] = int(dp[i-1][0] == 1 and obstacleGrid[i][0] == 0)

        # Fill the first row of the DP table
        for j in range(1, n):
            # A cell in the first row is reachable only if there is no obstacle 
            # and the cell to its left is reachable
            dp[0][j] = int(dp[0][j-1] == 1 and obstacleGrid[0][j] == 0)

        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                # A cell is reachable if there is no obstacle in it and
                # it can be reached either from the cell above or to its left
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The bottom-right corner contains the total number of unique paths
        return dp[m-1][n-1]

"""

Detailed Explanation
Initialization: The class Solution contains the method uniquePathsWithObstacles, which takes obstacleGrid as input. The dimensions of the grid are stored in m and n.

DP Table Creation: A 2D list dp of the same size as obstacleGrid is created. Each cell in dp will eventually contain the number of unique paths to that cell.

Starting Cell Check: If the starting cell (top-left corner) has an obstacle, the function immediately returns 0, as no path is possible.

Initialize Starting Point: The starting cell in the DP table is set to 1 since there is exactly one way to be at the starting point.

Fill First Column: The loop iterates over the first column of the DP table. A cell in this column is reachable if there's no obstacle and the cell above it is reachable. This is because movement is only allowed down or right.

Fill First Row: Similarly, the loop fills the first row of the DP table. A cell in this row is reachable if there's no obstacle and the cell to its left is reachable.

Fill Rest of DP Table: The nested loops fill the remaining cells of the DP table. A cell is reachable if it does not contain an obstacle and can be reached either from the cell directly above or from the cell to its left. The value of a cell in the DP table is the sum of the values of these two adjacent cells.

Return Result: The function returns the value of the bottom-right cell in the DP table, which represents the total number of unique paths from the top-left to the bottom-right corner, considering the obstacles.

Conclusion
This DP approach efficiently computes the number of unique paths by building up the solution using previously computed sub-problems. It ensures that each sub-problem is solved only once, resulting in an optimized solution compared to a naive recursive approach.
"""




if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))