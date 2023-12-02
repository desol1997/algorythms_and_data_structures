# Link to the leetcode problem: https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy1 = ListNode()
        dummy2 = ListNode()
        prev1 = dummy1
        prev2 = dummy2
        current = head
        while current is not None:
            if current.val < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            current = current.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        head = dummy1.next
        return head
