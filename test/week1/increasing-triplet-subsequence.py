class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstMin = float('inf')
        secondMin = float('inf')
        for i in range(len(nums)):
            if nums[i] <= firstMin:
                firstMin = nums[i]
            elif nums[i] <= secondMin:
                secondMin = nums[i]
            else:
                return True
        return False