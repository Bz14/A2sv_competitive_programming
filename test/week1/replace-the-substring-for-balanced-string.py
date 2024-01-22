class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        rem = ""
        res = float('inf')
        for ch in count:
            if count[ch] > len(s)//4:
                rem += (count[ch] - len(s)//4)*ch
        if rem == "":
            return 0
        remcount = Counter(rem)
        freq = Counter()
        j = 0
        for i in range(len(s)):
            freq[s[i]] += 1
            while remcount - freq == Counter():
                res = min(res, i - j + 1)
                freq[s[j]] -= 1
                j += 1
        return res