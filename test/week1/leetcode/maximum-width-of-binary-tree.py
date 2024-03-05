# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = defaultdict(list)
        maxWidth = 0

        def maximumWidth(node, width, height):
            if not node:
                return
            nodes[height].append(width)
            maximumWidth(node.left, (width * 2 + 1), height + 1)
            maximumWidth(node.right, (width * 2 + 2), height + 1)
        maximumWidth(root, 0, 0)
        for k, v in nodes.items():
            maxWidth = max(maxWidth, max(v) - min(v) + 1)
        return maxWidth