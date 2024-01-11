class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j = 0
        oddCount = 0
        niceCount = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                oddCount += 1
                niceCount = 0
            while oddCount == k:
                if nums[j] % 2 != 0:
                    oddCount -= 1
                j += 1
                niceCount += 1
            ans += niceCount
        return ans
