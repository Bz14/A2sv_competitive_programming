class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newStr = ''
        st = ''
        length = len(strs[0])
        for s in strs:
            length = min(length, len(s))
        for i in range(length):
            st = strs[0][i]
            count = 0
            for s in strs:
                if st == s[i]:
                    count += 1
            if count == len(strs):
                newStr += st
            else:
                break
        return newStr

        