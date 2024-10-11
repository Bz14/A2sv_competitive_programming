# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

n, k = list(map(int, input().split()))
energy = list(map(int, input().split()))
 
 
def check(x):
    need = 0
    gain = 0
 
    for eng in energy:
        if eng > x:
            diff = eng - x 
            gain += (diff - diff * k / 100)
        if eng < x:
            need += (x - eng)
    return gain >= need
 
 
l = min(energy)
r = max(energy)
 
while r - l > 10 ** -7:
    mid = (l + r) / 2
    if check(mid):
        l = mid
    else:
        r = mid
 
print(r)