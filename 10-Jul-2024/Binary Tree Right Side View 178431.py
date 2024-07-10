# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        if root:
            ans.append(root.val)
        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node and node.left:
                    nodes.append(node.left.val)
                    queue.append(node.left)
                if node and node.right:
                    nodes.append(node.right.val)
                    queue.append(node.right)           
            if nodes:
                ans.append(nodes[-1])
        return ans

            