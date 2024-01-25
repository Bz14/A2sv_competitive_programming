# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = head
        prev = None
        while node != slow:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        if fast:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True