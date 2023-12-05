class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for i in range(len(words)):
            word = words[i].lower()
            char = word[0]
            index = 0
            for j in range(len(keyboard)):
                if char in keyboard[j]:
                    index = j
                    break
            for ch in word:
                if ch not in keyboard[index]:
                    break
            else:
                result.append(words[i])
        return result
            
            