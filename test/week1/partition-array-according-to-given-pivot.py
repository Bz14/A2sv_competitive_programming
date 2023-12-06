class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessArr = []
        equalArr = []
        greaterArr = []
        for num in nums:
            if num < pivot:
                lessArr.append(num)
            elif num > pivot:
                greaterArr.append(num)
            else:
                equalArr.append(num)
        return lessArr + equalArr + greaterArr

