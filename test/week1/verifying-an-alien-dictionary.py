class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {}
        for i in range(len(order)):
            alpha[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if alpha[word1[j]] > alpha[word2[j]]:
                    return False
                elif alpha[word1[j]] < alpha[word2[j]]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True