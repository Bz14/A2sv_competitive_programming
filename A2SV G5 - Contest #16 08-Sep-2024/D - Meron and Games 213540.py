# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

import sys, threading
from collections import Counter
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    memo = {}
    count = Counter(arr)
    maxVal = max(arr)

    def dp(num):
        if num in memo:
            return memo[num]
        if num > maxVal:
            return 0
        val = max(num * count[num] + dp(num + 2), dp(num + 1))
        memo[num] = val
        return memo[num]
    print(dp(min(arr)))
        
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
