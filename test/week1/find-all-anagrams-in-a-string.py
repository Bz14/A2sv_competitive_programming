class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        s_count = [0] * 26
        l = 0
        res = []
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
        if p_count == s_count:
            res.append(l)
        for i in range(len(p), len(s)):
            s_count[ord(s[l]) - ord('a')] -= 1
            s_count[ord(s[i]) - ord('a')] += 1
            l += 1
            if p_count == s_count:
                res.append(l)
        return res
