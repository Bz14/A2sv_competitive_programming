# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = node = head
        while current and current.next:
            total = 0
            current = current.next
            while current and current.val != 0:
                total += current.val
                current = current.next
            if current:
                node = node.next
                node.val = total
        node.next = None
        return head.next