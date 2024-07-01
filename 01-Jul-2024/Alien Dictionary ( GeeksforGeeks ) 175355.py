# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        #code here
        graph = {chr(i + 97): [] for i in range(k)}
        in_degree = {chr(i + 97): 0 for i in range(k)}
        for i in range(N-1):
            min_len = min(len(alien_dict[i]), len(alien_dict[i + 1]))
            for j in range(min_len):
                if alien_dict[i][j] != alien_dict[i + 1][j]:
                    graph[alien_dict[i][j]].append(alien_dict[i + 1][j])
                    in_degree[alien_dict[i + 1][j]] += 1
                    break
        queue = deque([i for i in graph if in_degree[i] == 0])
        ans = []
        while queue:
            word = queue.popleft()
            ans.append(word)
            for child in graph[word]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        if len(ans) == k:
            return ans
        else:
            return []