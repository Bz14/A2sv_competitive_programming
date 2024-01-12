class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        currentVal = 0
        n = len(cardPoints)
        for i in range(n - k):
            currentVal += cardPoints[i]
        maxVal = total - currentVal
        for i in range(n - k, len(cardPoints)):
            currentVal += cardPoints[i]
            currentVal -= cardPoints[i - (n - k)]
            maxVal = max(maxVal, total - currentVal)
        return maxVal