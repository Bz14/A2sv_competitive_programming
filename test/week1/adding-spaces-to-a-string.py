class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        index = 0
        for space in spaces:
            res.append(s[index:space])
            res.append(' ')
            index = space
        res.append(s[index:])
        return ''.join(res)
