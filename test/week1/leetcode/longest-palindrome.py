class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        oddCount = 0
        for value in count.values():
            res += value
            if value % 2 != 0:
                oddCount += 1
        return res if oddCount == 0 else res - oddCount + 1