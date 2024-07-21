# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        ans = 0
        mask = 0
        for w in word:
            mask ^= 1 << (ord(w) - ord('a'))
            ans += prefix_map[mask]
            for i in range(10):
                pre_mask = mask ^ (1 << i)
                ans += prefix_map[pre_mask]
            prefix_map[mask] += 1
        return ans