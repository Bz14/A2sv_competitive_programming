class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r  = l + 1
        count = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
                count += 1
            r += 1
        return count