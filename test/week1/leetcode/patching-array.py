class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        idx = 0
        unmatched = 1
        while unmatched < n + 1:
            if idx < len(nums) and nums[idx] <= unmatched:
                unmatched += nums[idx]
                idx += 1
            else:
                patch += 1
                unmatched *= 2
        return patch