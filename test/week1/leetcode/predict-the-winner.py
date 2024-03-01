class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def checkWinner(l , r, turn):
            if turn:
                if l == r:
                    return nums[l]
                leftScore = checkWinner(l + 1, r, False) + nums[l]
                rightScore = checkWinner(l, r - 1, False) + nums[r]
                return max(leftScore, rightScore)
            else:
                if l == r:
                    return -nums[l]
                leftScore = checkWinner(l + 1, r, True) - nums[l]
                rightScore = checkWinner(l, r - 1, True) - nums[r]
                return min(leftScore, rightScore)
        ans = checkWinner(0, len(nums) - 1, True)
        return ans >= 0                

