# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[float("inf") for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            distances[u][v] = distances[v][u] = w

        for i in range(n):
            distances[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        ans = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and distances[i][j] <= distanceThreshold:
                    ans[i] += 1
        idx = 0
        minVal = ans[0]
        for i, count in enumerate(ans):
            if count <= minVal:
                minVal = count
                idx = i
        return idx