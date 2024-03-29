class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque([i for i in range(n)])
        res = 0
        while queue:
            for i in range(len(queue)):
                val = queue.popleft()
                tickets[val] -= 1
                if tickets[val] > 0:
                    queue.append(val)
                res += 1
                if tickets[k] == 0:
                    return res