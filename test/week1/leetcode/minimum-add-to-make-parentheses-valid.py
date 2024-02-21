class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for st in s:
            if st == "(":
                stack.append(st)
            elif st == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(st)
        return len(stack)
        