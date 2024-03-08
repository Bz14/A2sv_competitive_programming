# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        def BST(l, r):
            if l == r:
                return TreeNode(nodes[l])
            if l > r:
                return
            mid = (r + l) // 2
            root = TreeNode(nodes[mid])
            leftTree = BST(l, mid - 1)
            rightTree = BST(mid + 1, r)
            root.left = leftTree
            root.right = rightTree
            return root
        dfs(root)
        return BST(0, len(nodes) - 1)