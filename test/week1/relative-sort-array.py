class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lookup = {}
        for i, val in enumerate(arr2):
            lookup[val] = i
        for i in range(len(arr1)):
            for j in range(len(arr1) - i - 1):
                if lookup.get(arr1[j], 1001) > lookup.get(arr1[j + 1], 1001):
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                elif lookup.get(arr1[j], 1001) == lookup.get(arr1[j + 1], 1001):
                    if arr1[j] > arr1[j + 1]:
                        arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
        return arr1
                