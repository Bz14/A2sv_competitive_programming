class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitCount =  defaultdict(int)
        total = 0
        maxFruit = 0
        j = 0
        for i in range(len(fruits)):
            fruitCount[fruits[i]] += 1
            total += 1
            while len(fruitCount) > 2:
                fruitCount[fruits[j]] -= 1
                total -= 1
                if fruitCount[fruits[j]] == 0:
                    del fruitCount[fruits[j]]
                j += 1
            maxFruit = max(maxFruit, total)
        return maxFruit