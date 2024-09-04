"""
Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        res = s * 1.0
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            res = max(res, s)

        return res/k


## Test-case
nums = [1,12,-5,-6,50,3]
k = 4
expected = 12.75000
t1 = Solution()
result = t1.findMaxAverage(nums, k)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

