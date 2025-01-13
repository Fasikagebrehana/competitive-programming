class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        summ = 0
        for key, val in counter.items():
            if val >= 3:
                if val % 2 == 0:
                    summ += 2
                else:
                    summ += 1
            else:
                summ += val

        # print(counter)
        return summ