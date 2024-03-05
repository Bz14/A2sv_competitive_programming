class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(idx):
            if len(path) == k:
                ans.append(path[:])
                return
            if idx > n:
                return
            
            path.append(idx)
            backtrack(idx + 1)
            path.pop()

            backtrack(idx + 1)

        backtrack(1)
        return ans
