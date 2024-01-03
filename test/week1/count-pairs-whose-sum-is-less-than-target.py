class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        nums.sort()
        pairCount = 0
        while l < r:
            if nums[l] + nums[r] < target:
                pairCount += r - l
                l += 1
            else:
                r -= 1
        return pairCount