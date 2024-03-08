class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        res = 0

        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] + nums[i] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            l -= 1
            if l >= i:
                res += ((2 ** (l - i)) % mod)
        return res % mod
        