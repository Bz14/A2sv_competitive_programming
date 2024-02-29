# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        traverse(root)
        for i in range(len(ans) - 1):
            if ans[i] >= ans[i + 1]:
                return False
        return True