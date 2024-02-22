class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")
        stack = []
        ans = '/'
        for d in directory:
            if d != '.' and d != '..' and directory and d != '':
                stack.append(d)
            elif d == '..' and stack:
                stack.pop()
        ans += '/'.join(stack)
        return ans