class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kel, fahr = 0, 0
        kel = celsius + 273.15
        fahr = celsius * 1.80 + 32.00
        ans.append(kel)
        ans.append(fahr)
        return ans