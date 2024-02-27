class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index):
            k = ''
            st = ''
            while index < len(s):
                if s[index] == "[":
                    res = decode(index + 1)
                    st += int(k) * res[1]
                    k = ''
                    index = res[0]
                elif s[index] == "]":
                    return [index, st]
                elif s[index].isdigit():
                    k += s[index]
                else:
                    st += s[index]
                index += 1
            return [st, index]
        ans =  decode(0)
        return ans[0]