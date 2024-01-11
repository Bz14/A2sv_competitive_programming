class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        for i in range(k):
            if blocks[i] == "W":
                whiteCount += 1
        minCount = whiteCount
        j = 0
        for i in range(k, len(blocks)):
            if blocks[j] == "W":
                whiteCount -= 1
            if blocks[i] == "W":
                whiteCount += 1
            minCount = min(minCount, whiteCount)
            j += 1
        return minCount
