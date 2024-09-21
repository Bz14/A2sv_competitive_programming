# Problem: C - Spaceship Attack - https://codeforces.com/gym/511242/problem/C

n, m = list(map(int, input().split()))
spaceship = list(map(int, input().split()))
bases = []
for _ in range(m):
    value = list(map(int, input().split()))
    bases.append(value)
bases.sort()
pre_sum = [0]
for i in range(m):
    pre_sum.append(pre_sum[-1] + bases[i][1])
ans = []
for s in spaceship:
    l = 0
    r = len(bases) - 1
    while l <= r:
        mid = (l + r) // 2
        if bases[mid][0] <= s:
            l = mid + 1
        else:
            r = mid - 1
    ans.append(pre_sum[r + 1])
print(*ans)
