class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        idx = 0
        total = 1
        while total < n + 1:
            if idx < len(nums) and nums[idx] <= total:
                total += nums[idx]
                idx += 1
            else:
                total *= 2
                patch += 1
        return patch    