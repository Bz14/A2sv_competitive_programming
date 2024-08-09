# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        tree = defaultdict(list)
        leaves = []
        ans = 0
        def DFS(node, parent):
            if node:
                tree[node].append(parent)
                tree[parent].append(node)
                DFS(node.left, node)
                DFS(node.right, node)
        DFS(root, None)
        for node in tree:
            if node and not node.left and not node.right:
                leaves.append(node)
        for leaf in leaves:
            queue = deque([(leaf, 0)])
            visited = set([leaf])
            while queue:
                node, length = queue.popleft()
                if length > distance:
                    break
                if node:
                    for child in tree[node]:
                        if child not in visited:
                            visited.add(child)
                            queue.append((child, length + 1))
                    if node != leaf and not node.left and not node.right:
                        ans += 1
        return ans//2