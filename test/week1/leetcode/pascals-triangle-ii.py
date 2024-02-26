class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        def recur(idx):
            if idx == 0:
                return [1]
            value = recur(idx - 1)
            ans.append(value)
            arr = [1]
            for j in range(1, len(ans[-1])):
                arr.append(ans[-1][j - 1] + ans[-1][j])
            arr.append(1)
            ans.append(arr)
            return ans[-1]
        v = recur(rowIndex)
        return v



        # ans = [[1]]
        # if rowIndex == 0:
        #     return [1]
        # else:
        #     for i in range(rowIndex):
        #         arr = [1]
        #         for j in range(1, len(ans[-1])):
        #             arr.append(ans[-1][j - 1] + ans[-1][j])
        #         arr.append(1)
        #         ans.append(arr)
        # return ans[rowIndex]