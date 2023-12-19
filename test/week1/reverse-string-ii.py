class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rev = ''
        i = 0
        while i < len(s):
            word = s[i: i + 2 * k]
            rev += word[0:k][::-1] + word[k:]
            i += 2 * k
        return rev