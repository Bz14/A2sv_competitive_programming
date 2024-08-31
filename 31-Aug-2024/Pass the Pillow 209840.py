# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        dir = 1
        while time > 0:
            if i == n:
                dir = -1
            if i == 1:
                dir = 1
            if dir == 1:
                i += 1
            else:
                i -= 1
            time -= 1
        return i
