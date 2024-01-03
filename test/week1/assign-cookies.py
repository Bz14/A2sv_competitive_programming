class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0
        r = 0
        maxCount = 0
        while l < len(g) and r <  len(s):
            if g[l] <= s[r]:
                maxCount += 1
                l += 1
            r += 1
        return maxCount
