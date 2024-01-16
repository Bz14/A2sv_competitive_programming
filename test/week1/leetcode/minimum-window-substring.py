class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res = ""
        length = len(s) + 1
        t_count = Counter(t)
        s_count = defaultdict(int)
        j = 0
        count = 0
        for i in range(len(s)):
            if s[i] in t_count:
                s_count[s[i]] += 1
                if s_count[s[i]] == t_count[s[i]]:
                    count += 1
                    while count == len(t_count):
                        if i - j + 1 < length:
                            length = i - j + 1
                            res = s[j:i + 1]
                        if s[j] in s_count:
                            s_count[s[j]] -= 1
                            if s_count[s[j]] < t_count[s[j]]:
                                count -= 1
                        j += 1
        return res
