# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = defaultdict(list)
        for str in strs:
            ls = [0]*26
            for s in str:
                ls[ord(s) - ord('a')] += 1
            anadict[tuple(ls)].append(str)
        return anadict.values()