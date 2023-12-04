class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       newStr = ''
       for i in range(min(len(word1), len(word2))):
           newStr += word1[i]
           newStr += word2[i]
       if len(word1) > len(word2):
           newStr += word1[len(word2):]
       elif len(word1) < len(word2):
            newStr += word2[len(word1):]
       return newStr