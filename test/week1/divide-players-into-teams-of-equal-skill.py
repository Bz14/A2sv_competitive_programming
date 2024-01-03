class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        chemistry = 0
        prevSum = 0
        while l < r:
            if l == 0:
                prevSum = skill[l] + skill[r]
                chemistry += skill[l] * skill[r]
            elif prevSum == skill[l] + skill[r]:
                chemistry += skill[l] * skill[r]
            else:
                return -1
            l += 1
            r -= 1
        return chemistry


