class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the least it can be is maximum number and the maximum it can be 
        # is the sum of the weights
        low = max(weights)
        high = sum(weights)
        def helper(middle):
            count = 1
            summ = 0
            for i in range(len(weights)):
                if summ + weights[i] > middle:
                    count += 1
                    summ = 0
                summ += weights[i]
            if count > days:
                return False
            return True

        while low <= high:
            middle = (low + high) // 2
            if helper(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low