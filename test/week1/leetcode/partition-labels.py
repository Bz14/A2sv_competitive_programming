class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = defaultdict(int)
        maxIndex = 0
        res = []
        count = 0
        for i in range(len(s)):
            index[s[i]] = i
        for i, st in enumerate(s):
            maxIndex = max(maxIndex, index[st])
            count += 1
            if i == maxIndex:
                res.append(count)
                count = 0
        return res