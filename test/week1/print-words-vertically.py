class Solution:
    def printVertically(self, s: str) -> List[str]:
        val = s.split()
        maxLen = 0
        for v in val:
            maxLen = max(maxLen, len(v))
        res = ['']*maxLen
        for i in range(maxLen):
            for v in val:
                if i < len(v):
                    res[i] += v[i]
                else:
                    res[i] += ' '
        return [r.rstrip() for r in res]

            