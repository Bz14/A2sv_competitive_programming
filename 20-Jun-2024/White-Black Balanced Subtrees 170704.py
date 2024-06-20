# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import sys
from collections import defaultdict

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    colors = sys.stdin.readline().strip()
    graph = defaultdict(list)
    val = 2
    ans = 0
    color = {}
    for i in range(n):
        color[i + 1] = [0, 0]
    for i in range(len(arr)):
        graph[arr[i]].append(val)
        val += 1
    stack = [(1, False)]
    while stack:
        node, isChecked = stack.pop()
        if not isChecked:
            stack.append((node, True))
            for child in graph[node]:
                stack.append((child, False))
        else:
            white = 0
            black = 0
            for child in graph[node]:
                white += color[child][0]
                black += color[child][1]
            if colors[node - 1] == 'W':
                white += 1
            else:
                black += 1
            if white == black:
                ans += 1
            color[node] = [white, black]
    print(ans)
