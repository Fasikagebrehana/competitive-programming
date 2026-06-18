class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # full circle is 360 degree and in 60 minutes 360/60 = 6 degree per minute
        # for hour angle => there are 12 hours so 360/12= 30 degree when changed to minutes 30/60 = 0.5 degree per minute the hour angle moves

        minute_angle = minutes * 6
        # for hour angle the minutes affects the position 
        hour_angle = 30 * (hour) + 0.5 * minutes
        diff = abs(minute_angle - hour_angle)

        return min(diff, 360 - diff)