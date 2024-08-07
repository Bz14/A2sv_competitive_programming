# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        words = [(k, v) for k, v in count.items()]
        words.sort(key=lambda x : x[1], reverse=True)
        ans = 0
        mult = 1
        for i in range(len(words)):
            _, v = words[i]
            ans += (mult * v)
            if (i + 1) % 8 == 0:
                mult += 1
        return ans
        