class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for st in s:
            if st in parenthesis:
                stack.append(st)
            elif len(stack) == 0 or st != parenthesis[stack.pop()]:
                return False
        return len(stack) == 0