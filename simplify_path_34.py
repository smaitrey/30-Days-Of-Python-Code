"""
 Simplify Path
Solved
Medium
Topics
Companies
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.


Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).


"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()

            elif portion == "." or not portion:
                continue

            else:
                stack.append(portion)

        final_str = "/" + "/".join(stack)
        return final_str




## Test-case
path = "/home/user/Documents/../Pictures"

expected = "/home/user/Pictures"

t1 = Solution()
result = t1.simplifyPath(path)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")

