"""
Prefix sum: https://leetcode.com/problems/corporate-flight-bookings/
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        first_seats = [0] * n
        last_seats = [0] * n
        res = [0] * n
        total = 0
        
        for i in range(len(bookings)):
            first = bookings[i][0]
            last = bookings[i][1]
            seats = bookings[i][2]
            
            first_seats[first-1] += seats
            last_seats[last-1] += seats
        
        for i in range(len(res)):
            total += first_seats[i]
            res[i] = total
            total -= last_seats[i]
        
        return res
