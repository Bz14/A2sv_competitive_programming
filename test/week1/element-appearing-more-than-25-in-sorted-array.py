class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        number_of_occurence = Counter(arr)
        for key, value in number_of_occurence.items():
            if value > len(arr) // 4:
                return key
        return arr[0]