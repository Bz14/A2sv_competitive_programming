# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [arr[0]]

        n = len(arr)
        for i in range(1, n):
            prefix_xor.append(prefix_xor[-1] ^ arr[i])
        ans = []

        for l, r in queries:
            if l - 1 >= 0:
                ans.append(prefix_xor[r] ^ prefix_xor[l - 1])
            else:
                ans.append(prefix_xor[r])
        
        return ans