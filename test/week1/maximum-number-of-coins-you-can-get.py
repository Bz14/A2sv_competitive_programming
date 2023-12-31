class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        maxCoin = 0
        for i in range(2 * (len(piles) // 3)):
            if i % 2 != 0:
                maxCoin += piles[i]
        return maxCoin
