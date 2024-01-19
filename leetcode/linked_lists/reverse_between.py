# Link to the leetcode problem: https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for _ in range(1, left):
            prev = prev.next
        current = prev.next
        for _ in range(right - left):
            move_to_node = current.next
            current.next = move_to_node.next
            move_to_node.next = prev.next
            prev.next = move_to_node
        head = dummy.next
        return head
    