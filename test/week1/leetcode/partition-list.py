# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        before = lessNode = ListNode(0)
        after = greaterNode = ListNode(0)
        while head:
            if head.val < x:
                lessNode.next = head
                lessNode = lessNode.next
            else:
                greaterNode.next = head
                greaterNode = greaterNode.next
            head = head.next
        greaterNode.next = None
        lessNode.next = after.next
        return before.next

        
        