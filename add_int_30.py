"""
Add to Array-Form of Integer

The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234


"""

from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        for i in range(len(num) - 1, -1, -1):
            carry, num[i] = divmod(num[i], 10)
            if i:
                num[i-1] += carry

        print("carery :", carry)
        if carry <= 9 and carry != 0:
            num.insert(0, carry)

        if carry > 9:
            while carry > 0:
                carry, i = divmod(carry, 10)
                num.insert(0, i)

        return num


## Test-case
num = [1,2,0,0]
k = 34
expected = [1,2,3,4]
t1 = Solution()
result = t1.addToArrayForm(num, k)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


