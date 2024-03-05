# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(l, r):
            if l == r:
                return TreeNode(nums[l])
            if l > r:
                return
            mid = (r + l) // 2
            root = TreeNode(nums[mid])
            leftTree = BST(l, mid - 1)
            rightTree = BST(mid + 1, r)
            root.left = leftTree
            root.right = rightTree
            return root
        return BST(0, len(nums) - 1)