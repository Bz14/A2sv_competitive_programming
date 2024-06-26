# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        ans = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def DFS(node):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    DFS(child)
        for i in range(n):
            if i not in visited:
                prev_len = len(visited)
                visited.add(i)
                DFS(i)
                res = len(visited) - prev_len
                ans += res * (n - len(visited))
        return ans
        