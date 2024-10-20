# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        check = defaultdict(int)
        n = len(arr)
        for i in range(n):
            check[arr[i] % k] += 1
        if check[0] % 2 != 0:
            return False
        for val in check:
            if val != 0 and check[val] != check[k - val]:
                return False
        return True