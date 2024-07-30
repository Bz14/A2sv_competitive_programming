# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        i = 0
        for num in nums:
            res = num
            number = 0
            prod = 1
            if num == 0:
                arr.append((mapping[0], i, res))
            else:
                while num > 0:
                    val = num % 10
                    number += prod * mapping[val]
                    num //= 10
                    prod *= 10
                arr.append((number, i, res))
            i += 1
        arr.sort()
        return [arr[i][2] for i in range(len(nums))]

