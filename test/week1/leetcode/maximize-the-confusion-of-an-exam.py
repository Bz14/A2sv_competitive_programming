class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        j = 0
        maxLen = 0
        count = 0
        for i in range(len(answerKey)):
            if answerKey[i] == "F":
                count += 1
            while count > k:
                if answerKey[j] == "F":
                    count -= 1
                j += 1
            maxLen = max(maxLen, i - j + 1)
        j = 0
        count = 0
        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                count += 1
            while count > k:
                if answerKey[j] == "T":
                    count -= 1
                j += 1
            maxLen = max(maxLen, i - j + 1)
        return maxLen