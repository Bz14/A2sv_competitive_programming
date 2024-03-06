class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        first = -1
        last = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return[first, last]