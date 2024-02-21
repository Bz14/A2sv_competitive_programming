class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        count = Counter(palindrome)
        if len(palindrome) == 1:
            return ''
        palindrome = list(palindrome)
        for i in range(len(palindrome)):
            if count['a'] == len(palindrome) - 1:
                continue
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[-1] = 'b'
        return ''.join(palindrome)