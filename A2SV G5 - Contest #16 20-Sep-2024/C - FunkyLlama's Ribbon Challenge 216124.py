# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

import sys, threading
def main():
    n,a,b,c = list(map(int, input().split()))
    memo = {}
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return float("-inf")
        maxVal = float("-inf")
        for i in [a, b, c]:
            maxVal = max(maxVal, 1 + dp(n - i))
        memo[n] = maxVal
        return memo[n]
    print(dp(n))

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()