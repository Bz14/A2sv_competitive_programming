# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if idx not in curr.children:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.count += 1
        curr.is_end = True
        
    def find(self, word):
        ans = 0
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if idx not in curr.children:
                return ans
            curr = curr.children[idx]
            ans += curr.count
        return ans
from sys import stdin
n = int(input())
arr = []
for _ in range(n):
    arr.append(stdin.readline().strip())
obj = Solution()
total = 0
for val in arr:
    obj.insert(val)
    total += len(val)
ans = 0
for val in arr:
    res = obj.find(val[::-1])
    ans += (n * len(val) + total) - (2 * res)
print(ans)


