class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
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
                m += 1
        """i , j , k = 0, len(nums) - 1, 0
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                k -= 1
            k += 1"""