class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 0
        turn = 1
        result = []
        while positive < len(nums) or negative < len(nums):
            if turn and positive < len(nums):
                if nums[positive] > 0:
                    result.append(nums[positive])
                    turn = 0
                positive += 1
            elif not turn and negative < len(nums):
                if nums[negative] < 0:
                    result.append(nums[negative])
                    turn = 1
                negative += 1
            if len(nums) == len(result):
                break
        return result


