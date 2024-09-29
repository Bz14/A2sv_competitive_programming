# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
n = len(graph)
colors = [-1 for _ in range(n + 1)]
colors[1]  = 0
stack = [1]
while stack:
    node = stack.pop()
    for vertex in graph[node]:
        if colors[vertex] == -1:
            if colors[node] == 0:
                colors[vertex] = 1
            else:
                colors[vertex] = 0
            stack.append(vertex)
numZeros = colors.count(0)
numOnes = colors.count(1)
print(numOnes * numZeros - (n - 1))
