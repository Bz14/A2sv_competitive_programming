# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.found = True
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if ans and node.val <= ans[-1]:
                self.found = False
            ans.append(node.val)
            traverse(node.right)
        traverse(root)
        return self.found