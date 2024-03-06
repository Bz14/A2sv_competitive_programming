class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        path = []
        ans = []
        length = len(nums)

        def combination(idx, target):
            if target == 0 and len(path) == k:
                ans.append(path[:])
                return
            if target < 0:
                return
            for i in range(idx, length):
                path.append(nums[i])
                combination(i + 1, target - nums[i])
                path.pop()

        combination(0, n)
        return ans
