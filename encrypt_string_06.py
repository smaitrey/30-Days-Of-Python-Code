"""
Find the Encrypted String

You are given a string s and an integer k. Encrypt the string using the following algorithm:

For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
Return the encrypted string.

Input: s = "dart", k = 3

Output: "tdar"

We can use the simulation method. For the
 ith character of the string, we replace it with the character at position (i+k) mod n
 of the string.

The time complexity is
, and the space complexity is
. Here,
 is the length of the string
.
"""

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        cs = list(s)
        n = len(s)
        for i in range(n):
            cs[i] = s[(i + k) % n]
        return "".join(cs)


## Test-case
s = "dart"
k = 3
expected = "tdar"
t1 = Solution()
result = t1.getEncryptedString(s, k)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")
