# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        ans = 0
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
                print(mask)
            arr.append(mask)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not arr[i] & arr[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
