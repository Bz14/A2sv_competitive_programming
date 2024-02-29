# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        def traverse(node, height):
            if not node:
                return node
            if len(nodes) == height:
                nodes.append([])
            nodes[height].append(node.val)
            traverse(node.left, height + 1)
            traverse(node.right, height + 1)
        traverse(root, 0)
        for i in range(len(nodes)):
            if i % 2 != 0:
                nodes[i] = nodes[i][::-1]
        return nodes