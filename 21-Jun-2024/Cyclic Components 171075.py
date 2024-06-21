# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict
n, m = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
visited = set()
ans = 0
def DFS(node):
    stack = [node]
    vis = set()
    while stack:
        node = stack.pop()
        if len(graph[node]) != 2:
            return False
        for child in graph[node]:
            if child not in vis:
                vis.add(child)
                visited.add(child)
                stack.append(child)
    return True
for node in graph:
    if node not in visited:
        visited.add(node)
        if len(graph[node]) > 1:
            found = DFS(node)
            if found:
                ans += 1
print(ans)


