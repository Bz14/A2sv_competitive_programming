class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        """l = 0
        r = len(nums) - 1
        m = 0
        while m <= r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            elif nums[m] == 0:
                nums[m], nums[l] = nums[l] , nums[m]
                l += 1
                m += 1
            else:
                m += 1"""