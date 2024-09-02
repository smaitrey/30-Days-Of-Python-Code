"""
Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        ans = 0
        for i in digits:
            ans += i * (10 ** n)
            n -= 1

        ans += 1
        res = []
        while ans > 0:
            rem = ans % 10
            ans = ans // 10
            res.append(rem)

        i = 0
        j = len(res) - 1
        for c in range(len(res) // 2):
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        
        return res


## Test-case
digits = [1,2,3]
expected = [1,2,4]
t1 = Solution()
result = t1.plusOne(digits)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

