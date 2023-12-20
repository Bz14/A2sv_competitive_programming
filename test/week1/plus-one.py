class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        res = []
        if digits[-1]  + 1 != 10:
            res.append(digits[-1] + 1)
        else:
            res.append(0)
            rem = 1
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] + rem != 10:
                res.append(digits[i] + rem)
                rem = 0
            else:
                res.append(0)
                rem = 1
        if digits[0] == 9 and rem == 1:
            res.append(1)
        return res[::-1]