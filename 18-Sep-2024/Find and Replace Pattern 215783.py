# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in range(len(words)):
            j = 0
            flag = True
            count_1 = Counter()
            count_2 = Counter()
            while j < len(pattern):
                if words[i][j] not in count_1 and pattern[j] not in count_2:
                    count_1[words[i][j]] = pattern[j]
                    count_2[pattern[j]] = words[i][j]
                elif pattern[j] in count_2:
                    if count_2[pattern[j]] != words[i][j]:
                        flag = False
                elif words[i][j] in count_1:
                    if count_2[words[i][j]] != pattern[j]:
                        flag = False
                j += 1
            if flag:
                ans.append(words[i])
        return ans 
