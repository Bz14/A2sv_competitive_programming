class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque(i for i in range(n))
        res = 0
        while queue:
            for i in range(n):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    queue.popleft()
                    queue.append(tickets[i])
                    res += 1
                if tickets[k] == 0:
                    return res