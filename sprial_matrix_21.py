"""
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res




## Test-case
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
expected =  [1,2,3,4,8,12,11,10,9,5,6,7]
t1 = Solution()
result = t1.spiralOrder(matrix)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")



