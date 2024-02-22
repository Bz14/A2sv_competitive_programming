class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for st in s:
            res = 0
            if st == '(':
                stack.append(st)
            elif stack[-1] == "(":
                stack.pop()
                stack.append("1")
            else:
                while stack[-1] != "(":
                    val = stack.pop()
                    res += int(val)
                stack.pop()
                stack.append(str(res * 2))
        res = sum([int(i) for i in stack])
        return res

                 