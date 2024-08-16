# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = arr.copy()
        for i in range(n):
            if i + arr[i] < n:
                dp[i + arr[i]] = max(dp[i + arr[i]], dp[i] + arr[i + arr[i]])
        print(max(dp))

main()