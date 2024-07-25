"""
Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        if not words:
            return 0

        return len(words[-1])


## Test-case
s = "Hello World"
expected = 5
t1 = Solution()
result = t1.lengthOfLastWord(s)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


