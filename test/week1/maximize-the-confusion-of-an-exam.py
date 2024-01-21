class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {'T':0, 'F':0}
        j = 0
        res = 0
        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            while min(count.values()) > k:
                count[answerKey[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res