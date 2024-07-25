"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


import collections
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m1 = collections.defaultdict(int)

        for num in nums:
            m1[num] += 1

        n = n // 2
        for key, value in m1.items():
            if value > n:
                return key

        return 0


## Test-case
nums = [2,2,1,1,1,2,2]
expected = 2
t1 = Solution()
result = t1.majorityElement(nums)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")
