class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        i = 0
        maxCount = 0
        zeroCount = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[j] == 0:
                    zeroCount -= 1
                j += 1
            maxCount = max(maxCount, i - j + 1)
            i += 1
        return maxCount