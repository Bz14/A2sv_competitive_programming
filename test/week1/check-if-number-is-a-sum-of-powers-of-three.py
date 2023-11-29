class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 1:
            if n % 3 == 2:
                return False
            n //= 3
        if n == 0 or n == 1:
            return True

        


        


       