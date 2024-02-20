class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        l = 0
        r = l + 1
        res = 0
        while l < len(s) and r < len(s):
            if s[l] == "0":
                l += 1
                r += 1
            else:
                if s[r] == "0":
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r += 1
                    res += r - l
                else:
                    r += 1
        return res