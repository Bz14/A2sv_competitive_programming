class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(2, n):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res
