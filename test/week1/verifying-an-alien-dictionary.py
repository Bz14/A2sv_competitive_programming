class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {}
        for i in range(len(order)):
            alpha[order[i]] = i
        i = 0
        j = i + 1
        while i < len(words) and j < len(words):
            for k in range(min(len(words[i]), len(words[j]))):
                if alpha[words[i][k]] > alpha[words[j][k]]:
                    return False
                elif alpha[words[i][k]] < alpha[words[j][k]]:
                    break
            else:
                if len(words[i]) > len(words[j]):
                    return False
            i += 1
            j += 1
        return True