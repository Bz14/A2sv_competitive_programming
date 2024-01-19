class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newStr = []
        st = ''
        length = min(list(map(len, strs)))
        for i in range(length):
            st = strs[0][i]
            count = 0
            for s in strs:
                if st == s[i]:
                    count += 1
            if count == len(strs):
                newStr.append(st)
            else:
                break
        return ''.join(newStr)

        