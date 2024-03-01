class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammer(n, k):
            if n == 1:
                return 0
            value = grammer(n - 1, ceil(k / 2))
            if k % 2 == 0:
                value += 1
            return value
        val = grammer(n, k)
        if val % 2 == 0:
            return 0
        return 1