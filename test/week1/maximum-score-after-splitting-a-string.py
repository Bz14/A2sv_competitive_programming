class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(st) for st in s]
        prefix_sum = [s[0]]
        res = []
        for i in range(1, len(s)):
            prefix_sum.append(prefix_sum[-1] + s[i])
        for i in range(len(prefix_sum) - 1):
            value =  (prefix_sum[-1] - prefix_sum[i]) + (i + 1 - prefix_sum[i])
            res.append(value)
        return max(res)
