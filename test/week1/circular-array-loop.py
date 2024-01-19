class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow, fast = i, i
            while nums[i] * nums[fast] > 0 and nums[i] * nums[((fast + nums[fast]) % len(nums))] > 0:
                slow = (slow + nums[slow]) % len(nums)
                val = (fast + nums[fast]) % len(nums)
                fast = (val + nums[val]) % len(nums)

                if slow == fast:
                    if slow == (slow + nums[slow]) % len(nums):
                        break
                    return True
            slow, sign = i, nums[i]
            while sign * nums[slow] > 0:
                next = (slow + nums[slow]) % len(nums)
                nums[slow] = 0
                slow = next
        return False