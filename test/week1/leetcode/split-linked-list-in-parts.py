# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        ans = []
        while current:
            n += 1
            current = current.next
        parts = n // k
        current = head
        for i in range(k):
            part = parts + 1 if i < (n % k) else parts
            if part == 0:
                ans.append(None)
            else:
                ans.append(current)
                for i in range(part - 1):
                    current = current.next
                next_node = current.next
                current.next = None
                current = next_node
        return ans