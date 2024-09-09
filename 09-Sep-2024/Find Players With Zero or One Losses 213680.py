# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchDict = defaultdict(list)
        for winner, loser in matches:
            if winner not in matchDict:
                matchDict[winner] = [1,0]
            else:
                matchDict[winner][0] += 1
            if loser not in matchDict:
                matchDict[loser] = [0,1]
            else:
                matchDict[loser][1] += 1
        winners = []
        losers = []
        for key, value in matchDict.items():
            if value[1] == 1:
                losers.append(key)
            if value[1] == 0:
                winners.append(key)
        winners.sort()
        losers.sort()
        return [winners, losers]