# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq

n = int(input())
query = []
for _ in range(n):
    arr  = input().split()
    query.append(arr)
heap = []
ans = []
for q in query:
    if q[0] == "removeMin":
        if heap:
            heapq.heappop(heap)
        else:
            ans.append("insert 1")
        ans.append("removeMin")
    elif q[0] == "insert":
        heapq.heappush(heap, int(q[1]))
        ans.append("insert " + str(q[1]))
    elif q[0] == "getMin":
        while heap and int(heap[0]) < int(q[1]):
            ans.append("removeMin")
            heapq.heappop(heap)
        if not heap or int(heap[0]) > int(q[1]):
            heapq.heappush(heap, int(q[1]))
            ans.append("insert " + str(q[1]))
        ans.append("getMin " + str(q[1]))
print(len(ans))
print(*ans, sep="\n")