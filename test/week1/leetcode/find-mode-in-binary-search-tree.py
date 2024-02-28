# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def count(node):
            if not node:
                return
            counter[node.val] += 1
            count(node.left)
            count(node.right)
        count(root)                        
        mode = max(counter.values())
        return [k for k,v in counter.items() if v == mode]
