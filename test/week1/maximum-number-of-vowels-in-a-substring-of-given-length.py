class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        vowelCount = 0
        maxCount = 0
        count = 0
        for i in range(len(s)):
            count += 1
            if s[i] in vowels:
                vowelCount += 1
            if count == k:
                maxCount = max(maxCount, vowelCount)
                if s[l] in vowels:
                    vowelCount -= 1
                l += 1
                count -= 1
        return maxCount
