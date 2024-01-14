class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       fruitCount = defaultdict(int)
       l = 0
       total = 0
       maxFruit = 0
       for i in range(len(fruits)):
           fruitCount[fruits[i]] += 1
           total += 1
           while len(fruitCount) > 2:
               fr = fruits[l]
               fruitCount[fr] -= 1
               total -= 1
               l += 1
               if  not fruitCount[fr]:
                   fruitCount.pop(fr)
           maxFruit = max(maxFruit, total)
       return maxFruit