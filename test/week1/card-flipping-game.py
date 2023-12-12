class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        counter = defaultdict(int)
        for i in range(len(fronts)):
            counter[fronts[i]] += 1
            counter[backs[i]] += 1
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in counter:
                del counter[fronts[i]]
        return min(counter.keys()) if len(counter) > 0 else 0