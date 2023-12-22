class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        isIncrease = True
        isDecrease = False
        for i in range(len(arr) - 1):
            if i == 0 and arr[i] > arr[i + 1]:
                return False
            if arr[i] == arr[i + 1]:
                return False
            if not isIncrease and arr[i] < arr[i + 1]:
                return False
            if arr[i] > arr[i + 1]:
                isIncrease = False
                isDecrease = True
        return isDecrease