"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while(top <= bot):
            row = (top + bot) // 2
            if(target > matrix[row][-1]):
                top = row + 1
            elif(target < matrix[row][0]):
                bot = row - 1
            else:
                break

        # target not found in any of the row
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        left = 0
        right = COLS - 1
        while(left <= right):
            pivot = (left + right) // 2
            if(matrix[row][pivot] == target):
                return True

            if(target < matrix[row][pivot]):
                right = pivot - 1
            else:
                left = pivot + 1

        return False




## Test-case
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
expected = True
t1 = Solution()
result = t1.searchMatrix(matrix, target)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")



