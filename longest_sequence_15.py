"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4

"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in numSet:
                length = 1
                while (i + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest



## Test-case
nums = [100,4,200,1,3,2]
expected = 4
t1 = Solution()
result = t1.longestConsecutive(nums)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

