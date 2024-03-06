# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aCount = 0
        bCount = 0
        current = headA
        while current:
            aCount += 1
            current = current.next
        current = headB
        while current:
            bCount += 1
            current = current.next
        currentA = headA
        currentB = headB
        if aCount > bCount:
            for i in range(aCount - bCount):
                currentA = currentA.next
        else:
            for i in range(bCount - aCount):
                currentB = currentB.next
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None
