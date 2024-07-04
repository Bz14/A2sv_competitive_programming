# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict

def divisor(prod):
    d = 2
    ans = []
    while d * d <= prod:
        while prod % d == 0:
            ans.append(d)
            prod //= d
        d += 1
    if prod > 1:
        ans.append(prod)
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = defaultdict(int)
    for num in nums:
        prime = divisor(num)
        for val in prime:
            count[val] += 1
    for val in count.values():
        if val % n != 0:
            print("NO")
            break
    else:
        print("YES")

