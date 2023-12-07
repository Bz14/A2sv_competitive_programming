class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        index = 0
        for space in spaces:
            res += s[index:space] + ' '
            index = space
        res += s[index:]
        return res
