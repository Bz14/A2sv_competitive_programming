class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        largest = nums[-1]
        n = len(nums)

        for i in range(n - 1, -1, -1):
            if nums[i] <= largest:
                largest = nums[i] 
                continue
            val = nums[i] // largest
            if nums[i] % largest == 0:
                count += (val - 1)
            else:
                op = val + 1
                count += (op - 1)
                largest = nums[i] // op
        return count
