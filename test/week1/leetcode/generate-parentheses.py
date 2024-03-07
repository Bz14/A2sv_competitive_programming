class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []

        def generate(openCount, closeCount):
            if openCount == closeCount == n:
                ans.append(''.join(path))
                return
            if closeCount < openCount:
                path.append(")")
                generate(openCount, closeCount + 1)
                path.pop()
            if openCount < n:
                path.append("(")
                generate(openCount + 1, closeCount)
                path.pop()
        generate(0, 0)
        return ans
            