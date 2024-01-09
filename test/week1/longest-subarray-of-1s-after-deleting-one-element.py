class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        j = 0
        maxOnes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[j] == 0:
                    zeroCount -= 1
                j += 1
            maxOnes = max(maxOnes, i - j)
        return maxOnes
