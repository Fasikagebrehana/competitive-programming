class Solution:
    def countLargestGroup(self, n: int) -> int:
        store = defaultdict(int)
        for i in range(1, n+1):
            if i < 10:
                store[i] += 1
            else:
                num = i
                summ = 0
                while num > 0:
                    summ += num % 10
                    num //= 10
                # print(summ)
                store[summ] += 1
        maxx = max(store.values())
        # print(maxx)
        count = 0
        for key, val in store.items():
            if val == maxx:
                count += 1
        return count