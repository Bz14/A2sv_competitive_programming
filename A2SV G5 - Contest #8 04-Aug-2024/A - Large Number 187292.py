# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

testcase = int(input())
for _ in range(testcase):
    n, d = list(map(int, input().split()))
    num = input()
    numStr = str(num)
    idx = 0
    while idx < n and int(numStr[idx]) >= d:
        idx += 1
    ans = numStr[:idx] + str(d) + numStr[idx:]
    print(ans)