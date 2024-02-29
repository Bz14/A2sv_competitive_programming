# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)

        def traverse(node, height):
            if not node:
                return node
            nodes[height].append(node.val)
            traverse(node.left, height + 1)
            traverse(node.right, height + 1)
        traverse(root, 0)
        ans = []
        for k, v in nodes.items():
            if k % 2 == 0:
                ans.append(v)
            else:
                ans.append(v[::-1])
        return ans