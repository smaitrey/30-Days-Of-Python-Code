"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snakeSize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snakeSize += 1
            else:
                tmp = nums[i]
                nums[i] = nums[i - snakeSize]
                nums[i - snakeSize] = tmp
        return nums


## Test-case
nums = [0,1,0,3,12]
expected = [1,3,12,0,0]
t1 = Solution()
result =t1.moveZeroes(nums)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

