class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        precompute = [0] * len(customers)
        summ = customers[0][1]
        precompute[0] = customers[0][0] + customers[0][1]
        for i in range(1, len(customers)):
            if -precompute[i-1] + customers[i][0] < 0:
                precompute[i] += precompute[i-1] + customers[i][1]
            else:
                precompute[i] = customers[i][1] + customers[i][0]
            summ += precompute[i] - customers[i][0]
        return summ / len(customers)