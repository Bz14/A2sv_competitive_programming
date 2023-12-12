class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        numbers = set(nums)
        ans = 0
        for num in nums:
            left = 0
            right = 0
            if num in visited:
                continue
            while num + right in numbers:
                visited.add(num + right)
                right += 1
            while num - left in numbers:
                visited.add(num - left)
                left += 1
            ans = max(ans, left + right - 1)
        return ans




        """ls = list(set(nums))
        ls.sort()
        maxVal = 0
        count = 1
        for i in range(len(ls) - 1):
            if ls[i] + 1 == ls[i + 1]:
                count += 1
            else:
                maxVal = max(maxVal, count)
                count = 1
        maxVal = max(maxVal, count)
        return maxVal if len(nums) > 0 else 0"""