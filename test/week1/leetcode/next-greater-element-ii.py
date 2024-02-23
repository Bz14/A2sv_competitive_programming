class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(2):
            for i, num in enumerate(nums):
                while stack and stack[-1][0] < num:
                    value = stack.pop()
                    ans[value[1]] = num
                stack.append((num, i))
        return ans