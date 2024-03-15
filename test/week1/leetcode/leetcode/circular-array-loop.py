class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        checked = set()
        for i in range(n):
            if i not in checked:
                new_check = set()
                while True:
                    if i in new_check:
                        return True
                    if i in checked:
                        break
                    checked.add(i)
                    new_check.add(i)
                    prev = i
                    i = (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                        break
        return False