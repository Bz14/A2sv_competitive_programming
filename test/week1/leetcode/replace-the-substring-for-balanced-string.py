class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        res = float('inf')
        j = 0
        for i in range(len(s)):
            count[s[i]] -= 1
            while j < len(s) and all(count[c] <= len(s) // 4 for c in count):
                res = min(res, i - j + 1)
                count[s[j]] += 1
                j += 1
        if res == float('inf'):
            return 0
        return res

        
