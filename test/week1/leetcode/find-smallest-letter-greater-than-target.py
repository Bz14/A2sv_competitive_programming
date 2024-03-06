class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        char = letters[0]

        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                char = letters[mid]
                r = mid - 1
        return char
