class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l].lower() != s[r].lower():
                if self.checkOrder(s[l].lower()):
                    l += 1
                elif self.checkOrder(s[r].lower()):
                    r -= 1
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True
    def checkOrder(self, letter):
        return not ((ord(letter) >= ord('a') and ord(letter) <= ord('z'))
                    or (ord(letter) >= ord('0') and ord(letter) <= ord('9')))