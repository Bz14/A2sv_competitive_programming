class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                count += 1
            i += 1
        return count