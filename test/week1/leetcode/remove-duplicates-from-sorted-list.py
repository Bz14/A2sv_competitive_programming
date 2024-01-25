# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            if prev and current.val == prev.val:
                prev.next = current.next
                current = prev.next
            else:    
                prev = current
                current = current.next
        return head
        