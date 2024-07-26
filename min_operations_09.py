"""
Minimum Operations to Exceed Threshold Value I

You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

Input: nums = [2,11,10,1,3], k = 10
Output: 3

"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for x in nums:
            if x < k:
                count += 1

        return count


## Test-case
nums = [2,11,10,1,3]
k = 10
expected = 3
t1 = Solution()
result = t1.minOperations(nums, k)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

