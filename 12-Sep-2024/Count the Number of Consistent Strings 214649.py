# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_count = Counter(allowed)
        count = 0

        for word in words:
            word_count = Counter(word)
            is_allowed = True
            for k in word_count:
                if k not in allowed_count:
                    is_allowed = False
            if is_allowed:
                count += 1
        return count
