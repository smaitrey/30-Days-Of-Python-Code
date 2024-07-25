"""
Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pivot = 0
        left = 0
        right = len(nums) - 1

        while(left <= right):
            pivot = left + (right - left)//2
            if(nums[pivot] == target):
                return pivot

            if(target < nums[pivot]):
                right = pivot - 1
            else:
                left = pivot + 1

        return left


## Test-case
nums = [1,3,5,6]
target = 5
expected = 2
t1 = Solution()
result = t1.searchInsert(nums, target)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")
