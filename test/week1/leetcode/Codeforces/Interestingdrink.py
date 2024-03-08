n = int(input())
amount = list(map(int, input().split()))
m = int(input())
coins = []
for _ in range(m):
    coin = int(input())
    coins.append(coin)
amount.sort()
def check(value):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if amount[mid] > value:
            r = mid - 1
        else:
            l = mid + 1
    return l

for coin in coins:
    val = check(coin)
    print(val)