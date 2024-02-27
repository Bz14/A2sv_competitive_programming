class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x
        if n == 0:
            return 1
        elif n % 2 == 0:
            val = self.myPow(x, n // 2)
            return val * val
        else:
            val = self.myPow(x, n // 2)
            return val * val * x
