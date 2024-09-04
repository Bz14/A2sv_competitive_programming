# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ''
        for c in s:
            st += str(ord(c) - ord('a') + 1)
        while k > 0:
            ans = 0
            for c in st:
                ans += int(c)
            st = str(ans)
            k -= 1
        return int(st)
        