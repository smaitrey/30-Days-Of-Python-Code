"""
Find Three Consecutive Integers That Sum to a Given Number
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

Input: num = 33
Output: [10,11,12]

"""

from typing import List
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        a = num // 3
        return [a -1, a, a + 1]

## Test-case
num = 33
expected = [10, 11, 12]
t1 = Solution()
result = t1.sumOfThree(num)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


