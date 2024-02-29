# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def maxDiff(node):
            if not node:
                return 0

            if node.left and node.right:
                minLeft, maxLeft = maxDiff(node.left)
                minRight, maxRight = maxDiff(node.right)
                self.ans = max(self.ans, abs(node.val - minLeft), abs(node.val - maxLeft))
                self.ans = max(self.ans, abs(node.val - minRight), abs(node.val - maxRight))
                return min(minLeft, minRight, node.val), max(maxLeft, maxRight, node.val)

            if node.left:
                minLeft, maxLeft = maxDiff(node.left)
                self.ans = max(self.ans, abs(node.val - minLeft), abs(node.val - maxLeft))
                return min(minLeft, node.val), max(maxLeft, node.val)

            if node.right:
                minRight, maxRight = maxDiff(node.right)
                self.ans = max(self.ans, abs(node.val - minRight), abs(node.val - maxRight))
                return min(minRight, node.val), max(maxRight, node.val)

            return node.val, node.val
        maxDiff(root)
        return self.ans


        # self.ans = 0
        # def maxDiff(node, maxVal, minVal):
        #     if not node:
        #         return 0
        #     self.ans = max(self.ans, max(abs(node.val - maxVal), abs(node.val - minVal)))
        #     maxVal = max(maxVal, node.val)
        #     minVal = min(minVal, node.val)
        #     maxDiff(node.left, maxVal, minVal)
        #     maxDiff(node.right, maxVal, minVal)
