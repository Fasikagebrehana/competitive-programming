class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def helper(num):
            nonlocal count
            if num == 1:
                return count
            if num % 2 == 0:
                count += 1
                return helper(num//2)
            else:
                count += 1
                num = num * 3 + 1
                return helper(num)
        arr = []
        for i in range(lo, hi+1):
            count = 0
            helper(i)
            arr.append((count, i))
        # print(arr)

        arr.sort()
        return arr[k-1][1]