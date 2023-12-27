class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        prefixValue = 0
        maxVal = 0
        for i in range(len(flips)):
            maxVal = max(maxVal, flips[i])
            if i == maxVal - 1:
                prefixValue += 1
        return prefixValue