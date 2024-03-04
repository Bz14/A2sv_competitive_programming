class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def backtrack(num):
            ans.append(path[:])

            for i in range(num, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return ans

