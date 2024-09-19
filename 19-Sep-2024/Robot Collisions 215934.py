# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        position_dict = {p:i for i, p in enumerate(positions)}
        positions.sort()
        stack = []
        for pos in positions:
            idx = position_dict[pos]
            if directions[idx] == "R":
                stack.append(idx)
            else:
                while stack and directions[stack[-1]] == "R" and healths[idx] > 0:
                    i = stack.pop()
                    if healths[idx] > healths[i]:
                        healths[i] = 0
                        healths[idx] -= 1
                    elif healths[idx] < healths[i]:
                        healths[idx] = 0
                        healths[i] -= 1
                        stack.append(i)
                    else:
                        healths[idx] = 0
                        healths[i] = 0
                if healths[idx]:
                    stack.append(idx)
        ans = [h for h in healths if h > 0]
        return ans