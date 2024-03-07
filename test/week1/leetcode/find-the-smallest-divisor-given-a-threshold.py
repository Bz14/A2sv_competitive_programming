class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            total = 0
            for num in nums:
                total += ceil(num / divisor)
            print(total)
            return total <= threshold

        l = 1
        r = max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l