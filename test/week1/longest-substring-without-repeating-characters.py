class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        i = 0
        j = 0
        maxLen = 0
        while j < len(s):
            if s[j] in lookup:
                maxLen = max(maxLen, j - i)
                while s[j] in lookup:
                    lookup.remove(s[i])
                    i += 1
                lookup.add(s[j])
            else:
                lookup.add(s[j])
            j += 1
        maxLen = max(maxLen, j - i)
        return maxLen