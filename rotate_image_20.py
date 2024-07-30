"""
Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                topLeft = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = topLeft

            right -= 1
            left += 1

        return matrix




##Test-case
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
t1 = Solution()
result = t1.rotate(matrix)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


