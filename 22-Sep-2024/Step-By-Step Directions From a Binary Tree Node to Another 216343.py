# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def DFS(root, path, find):
            if root and root.val == find:
                return True
            if root.left and DFS(root.left, path, find):
                path += 'L'
            elif root.right and DFS(root.right, path, find):
                path += 'R'
            return path
        path1 ,path2 = [], []
        DFS(root, path1, startValue)
        DFS(root, path2, destValue)
        print(path1, path2)
        while path1 and path2 and path1[-1] == path2[-1]:
            path1.pop()
            path2.pop()
        return "".join("U" * len(path1)) + "".join(reversed(path2))
