class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def permutation(idx):
            if len(path) == n:
                ans.append(path[:])
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                permutation(i + 1)
                path.pop()
        permutation(0)
        return ans
