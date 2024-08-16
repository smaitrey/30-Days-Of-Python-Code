"""
 Number of Arithmetic Triplets

 You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2

"""

# Brute Force

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if self.contains(nums, nums[i] + diff) and self.contains(nums, nums[i] + 2 * diff):
                counter += 1
        return counter

    def contains(self, nums: List[int], target: int) -> bool:
        return target in nums


# Hashmap

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = {}
        counter = 0
        for i in range(len(nums)):
            seen[nums[i]] = i
        for num in nums:
            if (num + diff) in seen and (num + 2 * diff) in seen:
                counter += 1
        return counter


# Set

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        numSet = set(nums)
        for num in nums:
            if (num + diff) in numSet and (num + 2 * diff) in numSet:
                counter += 1

        return counter

# Binary search

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for num in nums:
            if self.binarySearch(nums, num + diff) and self.binarySearch(nums, num + 2 * diff):
                counter += 1
        return counter

    def binarySearch(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False



