# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

t = int(input())
def in_bound(row, col, n, m):
    return 0<=row<n and 0<=col<m
for _ in range(t):
    n, m , k = list(map(int, input().split()))
    dp = [[ float("inf") for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            if in_bound(i - 1, j, n, m):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + j + 1)
            if in_bound(i, j - 1, n, m):
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + i + 1)
    if dp[n - 1][m - 1] == k:
        print("YES")
    else:
        print("NO")




    
                