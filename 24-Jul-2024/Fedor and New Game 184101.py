# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = list(map(int, input().split()))
arr = []
for _ in range(m + 1):
    arr.append(int(input()))
player1 = arr[-1]
ans = 0
for i in range(m):
    player2 = arr[i]
    maxVal = max(player1, player2)
    val = 1
    idx = 0
    count = 0
    while val <= maxVal:
        val = 1 << idx
        if player1 & val != 0 and player2 & val == 0:
            count += 1
        if player1 & val == 0 and player2 & val != 0:
            count += 1
        idx += 1
    if count <= k:
        ans += 1
print(ans)

        

