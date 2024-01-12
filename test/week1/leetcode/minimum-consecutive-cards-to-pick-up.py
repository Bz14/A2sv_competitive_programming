class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lookup = defaultdict()
        minRes = float('inf')
        for i in range(len(cards)):
            if cards[i] in lookup:
                minRes = min(minRes, i - lookup[cards[i]] + 1)
            lookup[cards[i]] = i
        if minRes == float('inf'):
            return -1
        return minRes