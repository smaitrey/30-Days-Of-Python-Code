"""
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


## Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        smallAns = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return smallAns


## Test-case
head = [1,2,3,4,5]
expected = [5,4,3,2,1]
t1 = Solution()
result = t1.reverseList(head)
print(f"Test case: {'Passed' if result == expected else 'Failed'} (Expected: {expected}, Got: {result})")


