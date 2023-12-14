class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.arr = defaultdict()
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.arr[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        expireTime = currentTime - self.time
        if tokenId in self.arr and self.arr[tokenId] > expireTime:
            self.arr[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        expireTime = currentTime - self.time
        for key in self.arr:
            if self.arr[key] > expireTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)