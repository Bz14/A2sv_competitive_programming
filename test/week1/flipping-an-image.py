class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            arr = []
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    arr.append(1)
                else:
                    arr.append(0)
            res.append(arr[::-1])
        return res