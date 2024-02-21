class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n
        for i in range(n, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        # max_jump = 0
        # for i in range(len(nums)):
        #     if max_jump < i:
        #         return False
        #     max_jump = max(max_jump, i + nums[i])
        # return True
        