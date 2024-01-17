class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        check = [0]*(n + 1)
        for first, last, seat in bookings:
            check[first - 1] += seat
            check[last] -= seat
        prefix_sum = [check[0]]
        for i in range(1, len(check)):
            prefix_sum.append(prefix_sum[-1] + check[i])
        return prefix_sum[:-1]
        
        