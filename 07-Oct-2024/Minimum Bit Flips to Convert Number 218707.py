# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0

        for i in range(32):
            if (goal & (1 << i)) ^ (start & (1 << i)):
                count += 1
        return count