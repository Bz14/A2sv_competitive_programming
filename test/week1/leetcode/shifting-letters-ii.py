class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        check = [0]*(len(s) + 1)
        res = []
        for i,j,k in shifts:
            if k == 0:
                check[i] -= 1
                check[j + 1] += 1
            else:
                check[i] += 1
                check[j + 1] -= 1
        prefix_sum = [check[0]]
        for i in range(1, len(check)):
            prefix_sum.append(prefix_sum[-1] + check[i])
        for i in range(len(prefix_sum) - 1):
            ch = prefix_sum[i] + ord(s[i])
            if ch > ord('z'):
                r = ch - ord('z') - 1
                r %= 26
                res.append(chr(ord('a') + r))
            elif ch < ord('a'):
                r = ord('a') - ch - 1
                r %= 26
                res.append(chr(ord('z') - r))
            else:
                res.append(chr(ch))
        return ''.join(res)