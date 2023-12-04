class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = {}
        res = ''
        count = 1
        for i in range(ord('a'), ord('i') + 1):
            alpha[str(count)] = chr(i)
            count += 1
        count = 10
        for i in range(ord('j'), ord('z') + 1):
            alpha[str(count) + '#'] = chr(i)
            count += 1
        i = 0
        while i < len(s):
            if s[i : i + 3] in alpha:
                res += alpha[s[i: i + 3]]
                i += 3
            else:
                res += alpha[s[i]]
                i += 1
        return res

