"""
Check if Every Row and Column Contains All Numbers

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true

"""

from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            s = set()
            for j in range(n):
                s.add(matrix[i][j])
            if(len(s) != n):
                return False

        for i in range(n):
            s = set()
            for j in range(n):
                s.add(matrix[j][i])
            if(len(s) != n):
                return False

        return True


## Test-case

matrix = [[1,2,3],[3,1,2],[2,3,1]]
expected = True
t1 = Solution()
result = t1.checkValid(matrix)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


