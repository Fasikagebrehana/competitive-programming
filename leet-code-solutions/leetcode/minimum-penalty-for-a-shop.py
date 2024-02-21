class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_closing_time = 0
        suffix = customers.count('Y')
        prefix = 0
        dic = {}
        for i in range(len(customers)):
            dic[i] = (prefix + suffix)
            if customers[i] == 'Y':
                suffix -= 1
            else:
                prefix += 1
        dic[i+1] = prefix
        temp = inf
        for key, val in dic.items():
            if val < temp:
                temp = val
                min_closing_time = key
        return min_closing_time
            