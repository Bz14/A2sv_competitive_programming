class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxVal = max([z for x,y,z in trips])
        prefix_sum =  [0] * (maxVal + 1)
        for num_of_passenger, start, end in trips:
            prefix_sum[start] += num_of_passenger
            prefix_sum[end] -= num_of_passenger
        for i in range(len(prefix_sum)):
            if i > 0:
                prefix_sum[i] += prefix_sum[i - 1] 
        for value in prefix_sum:
            if value > capacity:
                return False
        return True