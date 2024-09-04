"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2


"""

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n+1):
                s = 0
                for l in range(i, j):
                    s += nums[l]

                if s == k:
                    count += 1

        return count




## Test-case
nums = [1,1,1]
k = 2
expected = 2
t1 = Solution()
result = t1.subarraySum(nums, k)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")




"""
M2:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        asum = [0] * (n + 1)
        asum[0] = 0
        for i in range(1, n+1):
            asum[i] = asum[i-1] + nums[i-1]

        for i in range(n):
            for j in range(i+1, n+1):
                if(asum[j] - asum[i] == k):
                    count += 1

        return count




M3:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    count += 1


        return count



M4:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        # Use defaultdict to handle default values conveniently
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1

        for num in nums:
            sum += num
            if (sum - k) in prefix_sum_count:
                count += prefix_sum_count[sum - k]
            prefix_sum_count[sum] += 1

        return count




"""
