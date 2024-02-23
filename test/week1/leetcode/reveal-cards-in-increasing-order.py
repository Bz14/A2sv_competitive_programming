class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse = True)
        queue.append(deck[0])
        for i in range(1, len(deck)):
            num = queue.pop()
            queue.appendleft(num)
            queue.appendleft(deck[i])
        return list(queue)