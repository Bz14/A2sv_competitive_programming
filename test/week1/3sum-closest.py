class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        closeVal = 0
        res = float('inf')
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < res:
                    res = abs(total - target)
                    closeVal = total
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return closeVal
        return closeVal

