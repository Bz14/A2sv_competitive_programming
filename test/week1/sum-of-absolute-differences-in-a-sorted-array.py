class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        total = 0
        for num in nums:
            total += abs(num-nums[0])
        result.append(total)
        for i in range(1,n):
            res = nums[i]-nums[i-1]
            total += res*i
            total -= res * (n-i)
            result.append(total)
        return result 