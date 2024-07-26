"""
Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        si = start = end = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > maxSum:
                maxSum = currentSum
                start = si
                end = i

            if currentSum < 0:
                currentSum = 0
                si = i + 1

        for i in range(start, end+1):
            print(nums[i], end=" ")

        return maxSum


## Test-case
nums = [-2,1,-3,4,-1,2,1,-5,4]
expected = 6
t1 = Solution()
result = t1.maxSubArray(nums)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

