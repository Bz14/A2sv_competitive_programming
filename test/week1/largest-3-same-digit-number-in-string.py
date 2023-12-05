class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        res = 0
        i = 0
        while i < len(num) - 3 + 1:
            if len(set(num[i:i+3])) == 1:
                res = max(res, int(num[i:i+3]))
                result = str(res)
                i += 3
            else:
                i += 1
        return result if result != '0' else '0'*3
