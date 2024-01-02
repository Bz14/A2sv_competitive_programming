class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr)-1,-1,-1):
            maxIndex = i
            for j in range(i,-1,-1):
                if arr[maxIndex] < arr[j]:
                    maxIndex = j
            self.flip(maxIndex, arr)
            self.flip(i, arr)
            flips.append(maxIndex + 1)
            flips.append(i + 1)
        return flips

    def flip(self,end,arr):
        start = 0
        while(start < end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1