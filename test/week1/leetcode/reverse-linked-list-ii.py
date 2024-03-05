# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_node = ListNode(0)
        new_node.next = head
        current = new_node
        for _ in range(left - 1):
            current = current.next
        first = current.next
        last = first.next
        for _ in range(right - left):
            first.next = last.next
            last.next = current.next
            current.next = last
            last = first.next
        return new_node.next