# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        queue = deque([1])
        visited  = set([1])
        d = 0
        while queue:
            n = len(queue)
            for i in range(n):
                value = queue.popleft()
                for curr in range(value + 1, min(m**2, value + 6) + 1):
                    new_row = m - ((curr - 1) // m) - 1
                    new_col = (curr - 1) % m
                    if (m - 1 - new_row) % 2:
                        new_col = m - new_col - 1
                    if board[new_row][new_col] != -1:
                        curr = board[new_row][new_col]
                    if curr == m * m:
                        return d + 1
                    if curr not in visited:
                        visited.add(curr)
                        queue.append(curr)
            d += 1
        return -1