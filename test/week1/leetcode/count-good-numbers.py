class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        def myPow(num, n):
            if n == 0:
                return 1
            val = myPow(num, n // 2)
            if n % 2 == 0:
                return (val * val) % mod
            return (val * val * num) % mod

        even = myPow(4, (n // 2)) % mod
        idx = (n // 2) if n % 2 == 0 else (n // 2) + 1
        odd = myPow(5, idx) % mod
        return (even * odd) % mod