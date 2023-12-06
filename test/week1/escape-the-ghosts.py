class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        move = abs(target[0]) + abs(target[1])
        print(move)
        for x,y in ghosts:
            print(abs(target[0] - x) + abs(target[1] - y))
            if abs(target[0] - x) + abs(target[1] - y) <= move:
                return False
        return True