class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        res = []
        for num in nums:
            if num % 2 == 0:
                total += num
        for value, index in queries:
            if nums[index] % 2 == 0:
                total -= nums[index]
                nums[index] += value
                if nums[index] % 2 == 0:
                    total += nums[index]
            else:
                nums[index] += value
                if nums[index] % 2 == 0:
                    total += nums[index]
            res.append(total) 
        return res

