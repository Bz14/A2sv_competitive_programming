class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        res = 0
        prev = 0
        for i in range(n):
            if i % 7 == 0:
                prev += 1
                res = prev
            else:
              res += 1
            total = total + res
        return total
