class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        answer = [0] * len(s)
        for word in s:
            answer[int(word[-1]) - 1] = word[:len(word) - 1]
        return ' '.join(answer)