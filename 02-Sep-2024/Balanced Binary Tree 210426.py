# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def DFS(node):
            nonlocal isBalanced
            if not node:
                return 0
            left_val = DFS(node.left)
            right_val = DFS(node.right)
            if abs(left_val - right_val) > 1:
                isBalanced = False
            return 1 + max(left_val, right_val)
        DFS(root)
        return isBalanced
            
            
