class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        parts = []
        for i in range(n - 1):
            parts.append(weights[i] + weights[i + 1])
        parts.sort()
        l = 0
        r = len(parts)- 1
        minVal = 0
        maxVal = 0
        for i in range(k - 1):
            minVal += parts[l]
            maxVal += parts[r]
            l += 1
            r -= 1
        return maxVal - minVal