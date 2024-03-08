# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        check = defaultdict(list)
        def dfs(node,row,col):
            if not node:
                return 
            check[(col, row)].append(node.val)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        check = dict(sorted(check.items(), key=lambda x : x[0]))
        for k, v in check.items():
            check[k] = sorted(v)
        new_dict = defaultdict(list)
        for k, v in check.items():
            for val in v:
                new_dict[k[0]].append(val)
        ans = [v for v in new_dict.values()]
        return ans
        