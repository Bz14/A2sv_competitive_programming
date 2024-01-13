class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        count = defaultdict(int)
        maxCount = 0
        res = 0
        for i in range(len(s)):
            count[s[i]] += 1
            maxCount = max(maxCount, count[s[i]])
            if i - j + 1 - maxCount > k:
                count[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res