class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        values = set()
        while n > 1:
            res = 0
            for v in str(number):
                res += int(v) ** 2
            if res in values:
                return False
            if res == 1:
                return True
            values.add(res)
            number = res
        return True
