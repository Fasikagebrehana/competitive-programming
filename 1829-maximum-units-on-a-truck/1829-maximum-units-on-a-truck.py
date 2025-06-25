class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key= lambda x : x[1], reverse = True)
        summ = 0
        max_unit = 0
        for boxes, units in boxTypes:
            if (summ + boxes) <= truckSize:
                max_unit += (boxes * units)
                summ += boxes
            else:
                if summ < truckSize:
                    max_unit += ((truckSize - summ) * units)
                    break
                else:
                    break
        return max_unit