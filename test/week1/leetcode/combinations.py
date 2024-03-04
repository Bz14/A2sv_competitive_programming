class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(idx):
            if len(path) == k:
                ans.append(path[:])

            for i in range(idx, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack(1)
        return ans
