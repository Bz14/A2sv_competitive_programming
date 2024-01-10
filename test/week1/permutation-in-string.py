class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        s2_counter = [0] * 26
        if len(s1) > len(s2):
            return False
        for s in s1:
            s1_counter[ord(s) - ord('a')] += 1
        j = 0
        for i in range(len(s2)):
            s2_counter[ord(s2[i]) - ord('a')] += 1
            if i - j + 1 == len(s1):
                if s1_counter == s2_counter:
                    return True
                s2_counter[ord(s2[j]) - ord('a')] -= 1
                j += 1
        return False