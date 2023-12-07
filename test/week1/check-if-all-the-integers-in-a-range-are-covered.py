class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        result = set()
        for num in range(left, right + 1):
            for start, end in ranges:
                values = {i for i in range(start, end + 1)}
                if num in values:
                    result.add(num)
        return len(result) == right - left + 1


            