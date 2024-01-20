class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        temp = [0] * (n+1)
        for first, last, seats in bookings:
            temp[first-1] += seats
            temp[last] -= seats
        
        for i in range(1,len(temp)):
            temp[i] += temp[i-1]
        return temp[:len(temp)-1]
        