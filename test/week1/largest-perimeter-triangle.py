class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result = 0
        nums.sort(reverse = True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                result = max(result, nums[i] + nums[i + 1] + nums[i + 2])
        return result
