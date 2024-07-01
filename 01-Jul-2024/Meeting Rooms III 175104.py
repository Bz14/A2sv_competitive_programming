# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        ans = [0 for _ in range(n)]
        heap1 = [i for i in range(n)]
        heap2 = []
        for start, end in meetings:
            while heap2 and heap2[0][0] <= start:
                _, room = heappop(heap2)
                heappush(heap1, room)
            if heap1:
                room = heappop(heap1)
                heappush(heap2, (end, room))
                ans[room] += 1
            else:
                end_time, room = heappop(heap2)
                new_time = end_time + (end - start)
                heappush(heap2, (new_time, room))
                ans[room] += 1
        print(ans)
        maxVal = max(ans)
        for i, val in enumerate(ans):
            if val == maxVal:
                return i