# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
n = int(input())
words = []
for _ in range(n):
    words.append(input())
graph = defaultdict(list)
in_degree = defaultdict(int)
for i in range(n - 1):
    found_diff = False
    minLen = min(len(words[i]), len(words[i + 1]))
    for j in range(minLen):
        if words[i][j] != words[i + 1][j]:
            graph[words[i][j]].append(words[i + 1][j])
            in_degree[words[i + 1][j]] += 1
            found_diff = True
            break
    if not found_diff and len(words[i]) > len(words[i + 1]):
            print("Impossible")
            exit()

ans = []
visited = set()

for i in range(26):
    char = chr(i + ord('a'))
    if in_degree[char] == 0 and char not in visited:
        queue = deque([char])
        while queue:
            node = queue.popleft()
            visited.add(node)
            ans.append(node)
            for child in graph[node]:
                in_degree[child] -= 1
                if child not in visited and in_degree[child] == 0 and ord(child) < ord(char):
                    queue.append(child)
                    visited.add(child)
if len(ans) == 26:
    print(''.join(ans))
else:
    print("Impossible")
